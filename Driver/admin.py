from django.contrib.admin import register , ModelAdmin
from .models import Drivers_info


@register(Drivers_info)
class Drivers_info_admin(ModelAdmin):
    list_display = ['first_name','last_name','code','personal_id','phone_number','motor_type']
    search_fields = ['first_name','last_name'] 
    list_filter = ['first_name','last_name','personal_id']
 #   autocomplete_fields = ['city','motor_type']
