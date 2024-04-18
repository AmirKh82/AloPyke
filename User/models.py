from typing import Any, Iterable
from django.db import models
from django.contrib.auth.models import User
import random

class Users_info(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    code = models.CharField(default=123 , max_length = 3)
    email = models.EmailField()
    personal_id = models.CharField(max_length=10,default =1234567890)
    city = models.CharField(
    max_length=10,
    choices = [
        ('TEH','Tehran'),
        ('MHD','Mshhad'),
        ('ESF','Esfahan'),
        ('Urmo','Urmia')
      ]
    )
    address = models.TextField()
    phone_number = models.CharField(max_length=11)
    user_type=models.CharField(
         choices = [
              ('person','person'),
              ('peyk','peyk'),
         ],
         max_length=10,
         default='person'
    )

    def __str__(self) -> str:
         return "{} - {} - {}".format(self.first_name , self.last_name , self.code)
    
    

class pyke_request(models.Model):
    user=models.ForeignKey(Users_info,on_delete=models.CASCADE)
    message = models.TextField()
    motor_type =  models.CharField(
        max_length=10,
        choices=[
            ('C50','C50'),
            ('BM','BMW'),
            ('HU','HIUNDA'),
            ('H2','HUNDA'),
            ('KH','KHAVTR')
        ],
        default='C50'
    )
    status = models.CharField(
        choices=[
            ('pending','pending'),
            ('accepted','accepted')
        ],
        max_length=100,
        default='pending'
    )

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        if self.status == 'accepted':
            self.user.user_type = 'peyk'
            self.user.save()
        return super().save()
    

 # user = models.ForeignKey(User, on_delete=models.PROTECT)

# class Meta:
#         verbose_name = "Kelaasor Flight"


class OTP(models.Model):
    phone_number = models.CharField(max_length=11)
    otp = models.CharField(max_length=5)



