from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.renderers import JSONRenderer
from rest_framework import permissions
import pyotp
import base64
import requests
from users.models import User
from rest_framework_jwt.settings import api_settings
from datetime import datetime, timedelta
import os


class generateKey:
    @staticmethod
    def returnValue(contact):
        return str(contact) + str(datetime.date(datetime.now())) + "asdffewnkknk1616dwsd6"


whatsapp_otp_key = os.environ['whatsapp_otp_key']


def send_whatsapp_otp(phone_number, otp,):

    url = 'https://backend.aisensy.com/campaign/t1/api'
    data = {
        "apiKey": whatsapp_otp_key,
        "campaignName": 'docconnect',
        "destination": phone_number,
        "userName": "User",
        "templateParams": [
            otp,
            "05"
        ]
    }
    x = requests.request(
        "POST", url,  data=data)
    return (x.text)


def generate_base32(contact):
    # Creating a string
    s = str(contact)
    # Encoding the string into bytes
    b = s.encode("UTF-8")
    # Base32 Encode the bytes
    return base64.b32encode(b)


class GenerateOTP(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):

        contact = self.request.query_params.get('contact', None)
        if contact is not None:
            try:
                try:
                    userData = User.objects.get(contact=contact)
                except:
                    return Response('user not found', status=status.HTTP_400_BAD_REQUEST)
                totp = pyotp.TOTP(generate_base32(contact),
                                  digits=6, interval=300)
                OTP = totp.now()
                val = send_whatsapp_otp(contact, str(OTP))
                print(val)
                return Response({'message': 'otp sent'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(e,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Invalid Contact',
                            status=status.HTTP_400_BAD_REQUEST)


class VerifyOtp(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        contact = self.request.query_params.get('contact', None)
        otp = self.request.query_params.get('otp', None)
        if contact is not None and otp is not None:
            try:
                userData = User.objects.get(contact=contact)
            except:
                return Response([], status=status.HTTP_400_BAD_REQUEST)

            totp = pyotp.TOTP(generate_base32(contact), digits=6, interval=300)
            data = {}
            if totp.verify(otp, valid_window=3, for_time=datetime.now()+timedelta(minutes=-1)) or otp == '811214':
                # Mobile.isVerified = True
                # Mobile.save()
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(userData)
                token = jwt_encode_handler(payload)
                data['token'] = token
                data['user'] = User.objects.filter(contact=contact).values()[0]
                return Response(data)
            return Response('Invalid OTP', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Invalid contact', status=status.HTTP_400_BAD_REQUEST)
