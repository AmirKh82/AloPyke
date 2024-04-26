from django.db import models
from User.models import Users_info
from typing import Any, Iterable


class Orders_info(models.Model):
    # this model for order information , which that gives you information about orders like price and duration and etc. 
    user = models.ForeignKey(Users_info,on_delete=models.CASCADE)
    origin = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)
    duration = models.TimeField()
    price = models.CharField(max_length=15,default='20')
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending','pending'),
            ('peyk_accepted','peyk_accepted')
    ],
    default='pending'
    )
    

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        if self.status == 'peyk_accepted':
            self.status = 'peyk_accepted'
            self.status.save()
        return super().save()


