import imp
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics
from messaging import sendsms
from random import randint
from django.db.models.signals import post_save
from user_app import serializer
from .models import User,otpModel
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
import datetime
# Create your views here.
class UserAPIView(generics.ListCreateAPIView):
    queryset=User.object.all()
    serializer_class=serializer.userSerializer

    @receiver(post_save, sender=User)
    def sendotp(sender,instance,**kwargs):
      if not instance.is_active:
            end =datetime.datetime.now() - datetime.timedelta(minutes=15)
            otps = otpModel.objects.filter(createdAt__lte=end)
            otps.delete()
            Otp = randint(100000, 999999)
            #print(instance.mobile)
            userOTP = otpModel(otp_value = Otp , user=instance)
            userOTP.save()
            if instance.mobile:
                sendsms(Otp,instance.mobile)
                #Response({'message':'otp is send','status':400})
      else:
          Response({'message':'user is active','status':400})

class userupdateAPIVIEW(generics.RetrieveUpdateDestroyAPIView):
        queryset=User.object.all()
        serializer_class=serializer.userSerializer
        lookup_field = 'id'



class otpViewAPIView(APIView):
    def get(self,request,email,sotp,format = None):
        #print(email)
        #print(sotp)
        user = get_object_or_404(User.objects.all(),email = email)
        #print(user.email)
        copt=get_object_or_404(otpModel.objects.all(),user=user.email)
        #print(copt.otp_value)
        if copt.otp_value==sotp:
            return Response({'message':'user is active','status':200})
        else:
            return Response({'message':'your Otp is wrong','status':200})         
        

