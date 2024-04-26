from rest_framework.serializers import ModelSerializer
from .models import Orders_info


class OrderSerializer(ModelSerializer):
    # # this serializer for the orders , that you can do all works about the order
    class Meta:
        model = Orders_info
        fields=['user','origin','destination','duration','price','status']
