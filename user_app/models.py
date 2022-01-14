
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import user_manager
from django.db.models.deletion import CASCADE

class User(AbstractUser):
    
    username=None
    email=models.EmailField(unique=True)
    email_token=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    forgot_password =models.CharField(max_length=100,null=True,blank=True)
    last_login_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    last_logout_time =models.DateTimeField(auto_now_add=True,null=True,blank=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    
    object=user_manager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email

class otpModel(models.Model):
    createdAt = models.TimeField(auto_now_add=True)
    otp_value=models.IntegerField(default=0)
    user = models.EmailField(max_length=100 , unique=True)

