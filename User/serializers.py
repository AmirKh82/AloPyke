from rest_framework.serializers import ModelSerializer
from .models import Users_info, pyke_request


class UserSerializer(ModelSerializer):
    class Meta:
        model = Users_info
        fields = ['first_name' , 'last_name' , 'user_type' , 'code' , 'personal_id'  ,'phone_number' ]
     

class PeykReqSerializer(ModelSerializer):
    class Meta:
        model =pyke_request
        fields = ['user','message','motor_type']


class PeykR2Serializer(ModelSerializer):
    class Meta:
        model =pyke_request 
        fields = ['user','motor_type','status']
        # list serlizer for peykreq


# class FlightSerializer(ModelSerializer):
#     origin = AirportSerializer()
#     destination = AirportSerializer()
#     class Meta:
#         model = Flight
#         fields = '__all__'


# class TicketSerializer(ModelSerializer):
#     reservation_code = CharField(required=False)
#     user = CharField(required=False)
#     class Meta:
#         model = Ticket
#         fields = '__all__'
        




