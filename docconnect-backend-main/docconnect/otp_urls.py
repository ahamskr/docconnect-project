from django.urls import path
from .otp import *


urlpatterns = [

    path('generate-otp/', GenerateOTP.as_view()),
    path('verify-otp/', VerifyOtp.as_view()),

]
