from django.urls import path
# from selectCar import views
from selectCar.views import Home

urlpatterns = [
       path('', Home.as_view(), name='home'),
]
