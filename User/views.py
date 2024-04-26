from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Users_info, pyke_request, OTP
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, PeykReqSerializer , PeykR2Serializer
import json , random
from .authentication import create_access_token, create_refresh_token
from django.contrib.auth.models import User


class UserInfoView(generics.ListAPIView):
    # in this view you can see the list of users 
    queryset= Users_info.objects.all()
    serializer_class = UserSerializer

class CreateUserView(generics.CreateAPIView):
    # in this view you can create a user 
    queryset= Users_info.objects.all()
    serializer_class = UserSerializer

class DeleteUserView(generics.DestroyAPIView):
    # in this view you can delete users 
    queryset = Users_info.objects.all()
    serializer_class = UserSerializer

class RetrieveUserView(generics.RetrieveAPIView):
    # in this view you can retrieve the users 
    queryset = Users_info.objects.all()
    serializer_class = UserSerializer

class UpdateUserView(generics.UpdateAPIView):
    # in this view you can update the users 
    queryset = Users_info.objects.all()
    serializer_class = UserSerializer

class ConversionUserView(generics.RetrieveUpdateDestroyAPIView):
     # in this view you can have a conversion on the users 
     queryset = Users_info.objects.all()
     serializer_class = UserSerializer

class CreatePeykReq(generics.CreateAPIView):
    # in this view you can create a request to be a peyk
    queryset= pyke_request.objects.all()
    serializer_class = PeykReqSerializer

class PeykReqList(generics.ListAPIView):
    # in this view you can see the list of PeykReq
    queryset= pyke_request.objects.all()
    serializer_class = PeykR2Serializer

class DeletePeykReq(generics.DestroyAPIView):
    # in this view you can delete PeykReq
    queryset = pyke_request.objects.all()
    serializer_class = PeykReqSerializer

class RetrievePeykReq(generics.RetrieveAPIView):
    # in this view you can retrieve PeykReq
    queryset = pyke_request.objects.all()
    serializer_class = PeykReqSerializer

class UpdatePeykReq(generics.UpdateAPIView):
    # in this view you can update the PeykReq
    queryset = pyke_request.objects.all()
    serializer_class = PeykReqSerializer

class ConversionPeykReq(generics.RetrieveUpdateDestroyAPIView):
     # in this view you can have a conversion on the PeykReq
     queryset = pyke_request.objects.all()
     serializer_class = PeykReqSerializer

class OTPView(APIView):

    # this view for generating OTP when you wana to enter
    def post(self, request):
        body = request.body
        body = json.loads(body)
        phone_number = body['phone_number']
        otp = random.randint(10000,99999)
        OTP.objects.create(
            phone_number = phone_number,
            otp = otp
        )
        return Response(otp)
    
class LoginView(APIView):

    # in this view you can login to the site 
    def post(self, request):
        body = request.body
        body = json.loads(body)
        phone = body['phone_number']
        otp = body['otp']
        try:
            saved_otp = OTP.objects.get(phone_number=phone)
            if saved_otp.otp == otp:
                saved_otp.delete()
                try:
                    current_user = User.objects.get(username=phone)
                except:
                    current_user = User.objects.create(
                        username = phone,
                    )
                access_token = create_access_token(current_user.id)
                refresh_token = create_refresh_token(current_user.id)
                res = Response(access_token)
                res.set_cookie('refresh_token', refresh_token, httponly=True)
                return res
            else:
                return Response("Otp is Wrong!", status=403)
        except:
            return Response("Something is Wrong!", status=500)

class SignUp(APIView):
    # in this view you can signup to the site 
    def post(self, request):
        body = request.body
        body = json.loads(body)
        signup = body['UserSerializer']
        Users_info.object.create(
            serializer_class = UserSerializer
            )
        signup.save()
        return(CreateUserView)    