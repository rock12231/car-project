from django.shortcuts import render
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'selectCar/index.html')
    
    
class Car(View):
    def get(self, request):
        car: dict = {
            'car_name': 'Toyota',
            'car_model': 'Corolla',
            'car_year': '2018',
            'car_price': '$100,000',
        }
        # take input data & send to the template
        return render(request, 'selectCar/car.html',{'car':car})
    
    def post(self, request):
        # select car & send to the template with the selected car info
        pass