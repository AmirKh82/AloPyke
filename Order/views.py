from rest_framework import generics
from .models import Orders_info
from .serializers import OrderSerializer 
import requests , json , datetime
from wsgiref import headers
from rest_framework.views import APIView
from rest_framework.response import Response
from User.authentication import JWTAuthentication

class OrderView(generics.CreateAPIView):
    # in this view you can create an order
    queryset = Orders_info.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication]

    def is_holyday(self):
        today = datetime.date.today()
        url = f'https://holidayapi.ir/gregorian/{today.year}/{today.month}/{today.day}'
        return requests.get(url).json()['is_holiday']

    def calculate_duration(origin, destination):
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
            print(duration)
        except:
            print("Error")


    calculate_duration(
        origin='35.6895266,51.2456417',
        destination='35.7160123,51.3620281'
    )

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):  
        price = self.calculate_duration * 10000
        price = price * 1.02 if self.is_holyday() else price 
        duration = self.calculate_duration 
        status = 'pending' 
        return super().perform_create(serializer)

class Orderlist(generics.ListAPIView):
    # you can see the orders list by this view
    queryset = Orders_info.objects.all()
    serializer_class = OrderSerializer

class OrderDelete(generics.DestroyAPIView):
    # # you can delete the orders by this view
    queryset = Orders_info.objects.all()
    serializer_class = OrderSerializer

class OrderRetrive(generics.RetrieveAPIView):
    # # you can retrieve orders by this view
    queryset = Orders_info.objects.all()
    serializer_class = OrderSerializer

class OrderUpdate(generics.UpdateAPIView):
    # # you can update the orders by this view
    queryset = Orders_info.objects.all()
    serializer_class = OrderSerializer

class OrderConversion(generics.RetrieveUpdateDestroyAPIView):
    # you can have a conversion on order by this view
    queryset = Orders_info.objects.all()
    serializer_class = OrderSerializer

class AcceptOrder(APIView):
    # peyk can accept the order 
    def post(self,request):
        body = request.body
        body = json.loads(body)
        order_id = body['order_id']
        order = Orders_info.objects.get(id=order_id)
        order.status='peyk_accepted'
        order.delete()
        return Response("Order Accepted")