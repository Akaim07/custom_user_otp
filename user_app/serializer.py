from django.db import models
from user_app.models  import User,otpModel
from rest_framework import serializers
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
           'id','email','mobile'
        )
class otpserializer(serializers.ModelSerializer):
     class Meta:
         model=otpModel
         fields='__all__'