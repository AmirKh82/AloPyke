from django.urls import path
from .views import info_D

urlpatterns = [
    #path('list', list ,name='list') ,
    path('information', info_D ,name='information_D')
]

