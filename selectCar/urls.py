from django.urls import path
from selectCar import views
from selectCar.views import Home, Car

urlpatterns = [
       path('', Home.as_view(), name='home'),
       path('car/', Car.as_view(), name='car'),
       
       # All Data pages cars list
       path('car/data1', views.data1, name='result1'),
       path('car/data2', views.data2, name='result2'),
       path('car/data3', views.data3, name='result3'),
       path('car/data4', views.data4, name='result4'),
       path('car/data5', views.data5, name='result5'),
       path('car/data6', views.data6, name='result6'),
       path('car/data7', views.data7, name='result7'),
       path('car/data8', views.data8, name='result8'),
       path('car/data9', views.data9, name='result9'),
       path('car/data10', views.data10, name='result10'),
]
