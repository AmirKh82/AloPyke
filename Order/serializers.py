from rest_framework.serializers import ModelSerializer
from .models import Orders_info


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Orders_info
        fields=['user','origin','destination']
        # ,'duration','price'
# du and price for request 

class OrderSerializer2(ModelSerializer):
    class Meta:
        model = Orders_info
        fields=['user','origin','destination','duration','price','status']
