from django.shortcuts import render
from .models import Drivers_info
from django.http import HttpResponse , JsonResponse

def info_D(request):
    information_of_drivers = Drivers_info.objects.all()
    info_of_driver = []
    for items in info_of_driver :
        dic = {
            'first_name' : Drivers_info.first_name ,
            'last_name' : Drivers_info.last_name ,
            'motor_type' : Drivers_info.motor_type ,
            'code' : Drivers_info.code ,
        }
        info_of_driver.append(dic)
    return HttpResponse(information_of_drivers)



