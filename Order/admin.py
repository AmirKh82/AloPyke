from django.contrib.admin import register , ModelAdmin
from .models import Orders_info
# Register your models here.

@register(Orders_info)
class Orders_info_admin(ModelAdmin):
    list_display = ['user','origin','destination','duration','price','status']
    search_fields = ['user','origin','destination','duration','price','status']
    list_filter = ['user','status']
    autocomplete_fields = ['user']