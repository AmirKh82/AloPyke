from django.contrib.admin import register, ModelAdmin
from .models import  Users_info, pyke_request, OTP


@register(Users_info)
class Users_info_admin(ModelAdmin):
    list_display = ['first_name','last_name','user_type','code','personal_id','phone_number']
    search_fields = ['first_name','last_name','code','personal_id','phone_number'] 
    list_filter = ['first_name','last_name','user_type','code','personal_id']
        

@register(pyke_request)
class pyke_request_admin(ModelAdmin):
    list_display = ['user','motor_type','status']
    search_fields = ['user','motor_type','status']
    list_filter = ['user','motor_type','status']
    autocomplete_fields = ['user']


@register(OTP)
class OtpAdmin(ModelAdmin):
    list_display = ['phone_number','otp']
    search_fields = ['phone_number','otp']
    list_filter = ['otp']
