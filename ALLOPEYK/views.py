from rest_framework import request 
from django.http import HttpResponse
import requests

def Welcome(request):
    return HttpResponse('welcome to this site , you can solve your traffic problem with this site , dont worry you can arrive early every day')

def About(request):
    return HttpResponse('here is about this site , this site is a transfer site , that you can a want a peyk and arrive to the home or work and etc . be with with us and achieve your goals , dont worry about the traffic ')

