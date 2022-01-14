import imp
from django.urls import path , include , re_path
from .views import otpViewAPIView,UserAPIView,userupdateAPIVIEW
urlpatterns = [
    path('User/',UserAPIView.as_view()),
    path('UserUpdate/<id>',userupdateAPIVIEW.as_view()),
    #path('DELETEUSER/',User_all_DeleteData.as_view())
    #path('OTPCHECK/<otp_value>',otpApiView.as_view())
    path('verify/<str:email>/<int:sotp>',otpViewAPIView.as_view())
]