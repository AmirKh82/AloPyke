from rest_framework.serializers import ModelSerializer
from .models import Users_info, pyke_request


class UserSerializer(ModelSerializer):
    # this serializer for the users , that you can do all works of users
    class Meta:
        model = Users_info
        fields = ['first_name' , 'last_name' , 'user_type' , 'code' , 'personal_id'  ,'phone_number' ]
     

class PeykReqSerializer(ModelSerializer):
    # this serialazer is about peykreq , that you can do all works of peykreq 
    class Meta:
        model =pyke_request
        fields = ['user','message','motor_type']


class PeykR2Serializer(ModelSerializer):
    # this serialazer for list of peykreq
    class Meta:
        model =pyke_request 
        fields = ['user','motor_type','status']

