from django.db import models


class Drivers_info(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    code = models.CharField(default=123,max_length=25)
    email = models.EmailField
    personal_id = models.CharField(max_length=10)
    city = models.CharField(
    max_length=10 ,
    choices = [
        ('TEH','Tehran'),
        ('MHD','Mshhad'),
        ('ESF','Esfahan'),
        ('Urmo','Urmia')
      ]  
    )
    address = models.TextField()
    phone_number = models.IntegerField()
    motor_type = models.CharField(
    max_length=10,
    choices = [
        ('C50','C50') ,
        ('HU','Hiunda') ,
        ('H2','Hunda') ,
        ('BM','Bmw') ,
        ('KH','Kavir') 
      ]
    )

    def __str__(self) -> str:
         return "{} - {}".format(self.first_name , self.last_name)