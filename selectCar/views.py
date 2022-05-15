from django.shortcuts import render
from django.views import View
import pandas as pd
import plotly.express as px
import json

df = pd.read_csv("selectCar/data/processed_cardekho.csv")

# Create your views here.
class Home(View):
    def get(self, request):
        # print("hello..........................................................")
        return render(request, 'selectCar/index.html')

class Car(View):
    def get(self, request):

        car: dict = {
            'car_name': 'Toyota',
            'car_model': 'Corolla',
            'car_year': '2018',
            'car_price': '$100,000',
        }
        
        tempDF = df.copy()

        if request.GET.get("Brand"):
            #msg=""
            #img select.
            tempDF = tempDF[tempDF["Brand"]==request.GET["Brand"]].sort_values('selling_price', ascending=False)

        if request.GET.get("year"):
            tempDF = tempDF[tempDF["year"] == int(request.GET["year"])].sort_values('selling_price', ascending=False)

        if request.GET.get("fuel"):
            tempDF = tempDF[tempDF["fuel"]==request.GET["fuel"]].sort_values('mileagev', ascending=False)

        tempDF = tempDF.head()
        # take input data & send to the template
        return render(request, 'selectCar/car.html',{'car':car, "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})
    
    def post(self, request):
        pass
#         1. What is the Best Mileage Car's with Brand name

# if request.GET.get("Brand"):
#    tempDF = tempDF[tempDF["Brand"]==request.GET["Brand"]].sort_values('mileagev', ascending=False)

# 2. Car's showcased according to the Selling Price Range (Min and Max)

# if request.GET.get("Min"):
#    tempDF = tempDF[(tempDF["mileagev"]>=request.GET["Min"])].sort_values('mileagev', ascending=False)

# if request.Get.get("Max"):
#    tempDF = tempDF[(tempDF["mileagev"]<=request.GET["Max"])].sort_values('mileagev', ascending=False)


# 3. The Highest Selling Price of that particular year?

# if request.GET.get("Year"):
#    tempDF = tempDF[tempDF["Year"]==request.GET["Year"]].sort_values('mileagev', ascending=False)

# 4. Which are the High Power and Low Selling Price car models?

# if request.GET.get("Year"):
#    tempDF = tempDF[tempDF["Year"]==request.GET["Year"]].sort_values('mileagev', ascending=False)

# 5. Which are the Max Mileage and Max Power car models?

# tempDF = tempDF.sort_values('mileagev', ascending=False).sort_values('max_powerv', ascending=False)

# 6. Which are the Max Engine and Max Power car models?

# tempDF = tempDF.sort_values('enginev', ascending=False).sort_values('max_powerv', ascending=False)


# 7. Which are the Max Mileage and Max Engine car models?

# tempDF = tempDF.sort_values('mileagev', ascending=False).sort_values('enginev', ascending=False)

# 8. The Best Mileage Car models are?

# tempDF = tempDF.sort_values('mileagev', ascending=False)
