from django.urls import path
from .views import( OrderView , Orderlist , OrderDelete,
OrderRetrive , OrderUpdate ,OrderConversion , AcceptOrder ,
)
urlpatterns = [
    path('create-order',OrderView.as_view(),name='creat-order'),
    path('order-list',Orderlist.as_view(),name='order-list'),
    path('delete-order/<int:pk>', OrderDelete.as_view(),name='delete-order'),
    path('retrive-order/<int:pk>', OrderRetrive.as_view(),name='retrive-order'),
    path('update-order/<int:pk>', OrderUpdate.as_view(),name='update-order'),
    path('conversion-order/<int:pk>', OrderConversion.as_view(),name='conversion-order'),
    path('peyk-accept', AcceptOrder.as_view(),name='peyk-accept')
]

