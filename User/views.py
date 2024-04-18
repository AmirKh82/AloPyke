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
    queryset= Users_info.objects.all()
    serializer_class = UserSerializer

class CreateUserView(generics.CreateAPIView):
    queryset= Users_info.objects.all()
    serializer_class = UserSerializer

class DeleteUserView(generics.DestroyAPIView):
    queryset = Users_info.objects.all()
    serializer_class = UserSerializer

class RetrieveUserView(generics.RetrieveAPIView):
    queryset = Users_info.objects.all()
    serializer_class = UserSerializer

class UpdateUserView(generics.UpdateAPIView):
    queryset = Users_info.objects.all()
    serializer_class = UserSerializer

class ConversionUserView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Users_info.objects.all()
     serializer_class = UserSerializer

class CreatePeykReq(generics.CreateAPIView):
    queryset= pyke_request.objects.all()
    serializer_class = PeykReqSerializer

class PeykReqList(generics.ListAPIView):
    queryset= pyke_request.objects.all()
    serializer_class = PeykR2Serializer

class DeletePeykReq(generics.DestroyAPIView):
    queryset = pyke_request.objects.all()
    serializer_class = PeykReqSerializer

class RetrievePeykReq(generics.RetrieveAPIView):
    queryset = pyke_request.objects.all()
    serializer_class = PeykReqSerializer

class UpdatePeykReq(generics.UpdateAPIView):
    queryset = pyke_request.objects.all()
    serializer_class = PeykReqSerializer

class ConversionPeykReq(generics.RetrieveUpdateDestroyAPIView):
     queryset = pyke_request.objects.all()
     serializer_class = PeykReqSerializer


#  code for sign up ???
class CodeView(APIView):

    def post(self, request):
        body = request.body
        body = json.loads(body)
        phone_number = body['phone_number']
        code = random.randint(10000,99999)
        Users_info.objects.create(
            phone_number = phone_number,
            code = code 
        )
        return Response(code)
    


    # class TicketList(generics.ListAPIView): -> tickect creat ?
    # queryset = Ticket.objects.all()
    # serializer_class = TicketSerializer
    # authentication_classes = [JWTAuthentication,]

    # def list(self, request, *args, **kwargs):
    #     self.queryset = Ticket.objects.filter(user=request.user)
    #     return super().list(request, *args, **kwargs)


   # flight ..........   ok  
     

class OTPView(APIView):

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
    
        
# class TicketCreate(generics.CreateAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
#     authentication_classes = [JWTAuthentication,]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         code = self.perform_create(serializer, request)
#         headers = self.get_success_headers(serializer.data)
#         return Response("Ticket Reserved with {} reservation code!".format(code), status=status.HTTP_201_CREATED, headers=headers)

#     def perform_create(self, serializer, request):
#         code = generate_reservation_code()
#         serializer.save(
#             reservation_code = code,
#             user = request.user
#         )
#         return code