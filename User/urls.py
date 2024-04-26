from django.urls import path
from .views import ( UserInfoView, CreateUserView, DeleteUserView, RetrieveUserView,
ConversionUserView,CreatePeykReq,PeykReqList,DeletePeykReq ,
RetrievePeykReq,UpdatePeykReq,ConversionPeykReq,OTPView,LoginView,UpdateUserView,
 SignUp
)
urlpatterns = [
    path('uers-list',UserInfoView.as_view(),name='uers-list'),
    path('create-user', CreateUserView.as_view(),name='create-user'),
    path('delete-user/<int:pk>', DeleteUserView.as_view(),name='delete-user'),
    path('retrive-user/<int:pk>', RetrieveUserView.as_view(),name='retrive-user'),
    path('update-user/<int:pk>', UpdateUserView.as_view(),name='update-user'),
    path('conversion-user/<int:pk>', ConversionUserView.as_view(),name='conversion-user'),
    path('peyk-req', CreatePeykReq.as_view(),name='peyk-req'),
    path('peyk-req-list', PeykReqList.as_view(),name='peyk-req-list'),
    path('delete-peyk-req/<int:pk>', DeletePeykReq.as_view(),name='delete-peyk-req'),
    path('retrive-peyk-req/<int:pk>', RetrievePeykReq.as_view(),name='retrive-peyk-req'),
    path('update-peyk-req/<int:pk>', UpdatePeykReq.as_view(),name='update-peyk-req'),
    path('conversion-peyk-req/<int:pk>', ConversionPeykReq.as_view(),name='conversion-peyk-req'),
    path('generate-otp', OTPView.as_view(), name='generate-otp'),
    path('login', LoginView.as_view(), name='login'),
    path('signup',SignUp.as_view,name='signup')
]
 