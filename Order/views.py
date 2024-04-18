from rest_framework import generics
from .models import Orders_info
from .serializers import OrderSerializer , OrderSerializer2
import requests , json , datetime
from wsgiref import headers


class OrderView(generics.CreateAPIView):
    queryset = Orders_info.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):  
        price = 10000 
        return super().perform_create(serializer)
    #  do we need JWTauth
    # why perform and create

    def is_holyday(self):
        today = datetime.date.today()
        url = f'https://holidayapi.ir/gregorian/{today.year}/{today.month}/{today.day}'
        return requests.get(url).json()['is_holiday']

    def calculate_price(self,origin, destination):
        try:
            api_key= 'service.b74073a6e66540fc9aa46f58aaa3f42b'
            url = 'https://api.neshan.org/v4/direction?type=motorcycle&origin={}&destination={}'.format(origin,destination)

            headers = {
                'Api-Key':api_key
            }

            resposne = requests.get(
                url=url,
                headers=headers
            )

            duration = resposne.json()['routes'][0]['legs'][0]['duration']['value']
            price = duration * 1000
            price = price * 1.02 if self.is_holyday() else price
            print("Duration is {} and price is {}".format(duration,price))
        except:
            print("Error")


    calculate_price(
        origin='35.6895266,51.2456417',
        destination='35.7160123,51.3620281'
    )




class Orderlist(generics.ListAPIView):
    queryset = Orders_info.objects.all()
    serializer_class = OrderSerializer2

class OrderDelete(generics.DestroyAPIView):
    queryset = Orders_info.objects.all()
    serializer_class = OrderSerializer2

class OrderRetrive(generics.RetrieveAPIView):
    queryset = Orders_info.objects.all()
    serializer_class = OrderSerializer

class OrderUpdate(generics.UpdateAPIView):
    queryset = Orders_info.objects.all()
    serializer_class = OrderSerializer

class OrderConversion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders_info.objects.all()
    serializer_class = OrderSerializer

    