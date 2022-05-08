from django.urls import path
# from selectCar import views
from selectCar.views import Home, Car

urlpatterns = [
       path('', Home.as_view(), name='home'),
       path('car/', Car.as_view(), name='car'),
]
