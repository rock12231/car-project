from ast import Str
from django.shortcuts import render
from django.views import View
import pandas as pd
import plotly.express as px
import json

df = pd.read_csv("selectCar/data/processed_cardekho.csv")

car: dict = {
            'car_name': 'Toyota',
            'car_model': 'Corolla',
            'car_year': '2018',
            'car_price': '$100,000',
            'brand': "",
            'year': "",
            'cars':""
            }
# Create your views here.
class Home(View):
    def get(self, request):
        # print("hello..........................................................")
        return render(request, 'selectCar/index.html')

class Car(View):
    def get(self, request):
        tempDF = df.copy() 
        tempOptions = tempDF["Brand"].unique()
        car['cars'] = tempOptions  
        tempDF = tempDF.head()
        return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})
    
    def post(self, request):       
        tempDF = df.copy()
        tempOptions = tempDF["Brand"].unique()
        car['cars'] = tempOptions
        
        # if request.POST["year"] and request.POST["Brand"]:
        #     tempOptions = tempDF["Brand"].unique()
        #     car['cars'] = tempOptions 
        #     car['brand'] = request.POST["Brand"]
        #     car['year'] = request.POST["year"]
        #     if car['brand'].isdigit():
        #         print(car['brand'],"YB................................")
        #         tempDF = tempDF[tempDF["year"]==request.POST["year"]].sort_values('selling_price', ascending=False)
        #         tempDF = tempDF.head()
        #     else:
        #         print(car['brand'],"YB................................")
        #         tempDF = tempDF[tempDF["Brand"]==request.POST["Brand"]].sort_values('selling_price', ascending=False)
        #         tempDF = tempDF.head()
        
        if request.POST["Brand"]:
            tempDF = tempDF[tempDF["Brand"]==request.POST["Brand"]].sort_values('selling_price', ascending=False)
            tempDF = tempDF.head()
            
        if request.POST["year"] and len(request.POST["year"])==4:
            print("Y................................")
            int_year = int(request.POST["year"])
            tempDF = tempDF[tempDF["year"]==int_year].sort_values('selling_price', ascending=False)
            tempDF = tempDF.head()
            
        if request.POST["year"] and len(request.POST["year"])>4:
            print("P................................")
            int_year = int(request.POST["year"])
            tempDF = tempDF[tempDF["selling_price"]<int_year].sort_values('mileagev', ascending=False)
            tempDF = tempDF.head()
        
        return render(request, 'selectCar/car.html',{"car":car, "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})
    
        
def data1(request):
    tempDF = df.copy()
    tempDF = tempDF.sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

def data2(request):
    tempDF = df.copy()
    tempDF = tempDF[(tempDF["mileagev"]>=request.GET["Min"])].sort_values('mileagev', ascending=False)
    tempDF = tempDF.sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

def data3(request):
    tempDF = df.copy()
    tempDF = tempDF[(tempDF["mileagev"]>=request.GET["Min"])].sort_values('mileagev', ascending=False)
    tempDF = tempDF.sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

def data4(request):
    tempDF = df.copy()
    tempDF = tempDF[(tempDF["mileagev"]>=request.GET["Min"])].sort_values('mileagev', ascending=False)
    tempDF = tempDF.sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

def data5(request):
    tempDF = df.copy()
    tempDF = tempDF[(tempDF["mileagev"]>=request.GET["Min"])].sort_values('mileagev', ascending=False)
    tempDF = tempDF.sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

def data6(request):
    tempDF = df.copy()
    tempDF = tempDF[(tempDF["mileagev"]>=request.GET["Min"])].sort_values('mileagev', ascending=False)
    tempDF = tempDF.sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

def data7(request):
    tempDF = df.copy()
    tempDF = tempDF[(tempDF["mileagev"]>=request.GET["Min"])].sort_values('mileagev', ascending=False)
    tempDF = tempDF.sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

def data8(request):
    tempDF = df.copy()
    tempDF = tempDF[(tempDF["mileagev"]>=request.GET["Min"])].sort_values('mileagev', ascending=False)
    tempDF = tempDF.sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

def data9(request):
    tempDF = df.copy()
    tempDF = tempDF[(tempDF["mileagev"]>=request.GET["Min"])].sort_values('mileagev', ascending=False)
    tempDF = tempDF.sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

def data10(request):
    tempDF = df.copy()
    tempDF = tempDF[(tempDF["mileagev"]>=request.GET["Min"])].sort_values('mileagev', ascending=False)
    tempDF = tempDF.sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})



   
    # def post(self, request):
    #     car: dict = {
    #         'car_name': 'Toyota',
    #         'car_model': 'Corolla',
    #         'car_year': '2018',
    #         'car_price': '$100,000',
    #     }
    #     tempDF = df.copy()
        
    #     # 1. What is the Best Mileage Car's with Brand name
    #     # if request.GET.get("Brand"):
    #         # tempDF = tempDF[tempDF["Brand"]==request.GET["Brand"]].sort_values('mileagev', ascending=False)
    #     # 2. Car's showcased according to the Selling Price Range (Min and Max)
    #     # if request.GET.get("Min"):
    #         # tempDF = tempDF[(tempDF["mileagev"]>=request.GET["Min"])].sort_values('mileagev', ascending=False)
    #     # if request.Get.get("Max"):
    #         # tempDF = tempDF[(tempDF["mileagev"]<=request.GET["Max"])].sort_values('mileagev', ascending=False)
    #     # 3. The Highest Selling Price of that particular year?
    #     # if request.GET.get("Year"):
    #         # tempDF = tempDF[tempDF["Year"]==request.GET["Year"]].sort_values('mileagev', ascending=False)
    #     # 4. Which are the High Power and Low Selling Price car models?
    #     # if request.GET.get("Year"):
    #         # tempDF = tempDF[tempDF["Year"]==request.GET["Year"]].sort_values('mileagev', ascending=False)
    #     # 5. Which are the Max Mileage and Max Power car models?
    #     # if request.GET.get("Q5"):
    #         # tempDF = tempDF.sort_values('mileagev', ascending=False).sort_values('max_powerv', ascending=False)
    #     # 6. Which are the Max Engine and Max Power car models?
    #     # if request.GET.get("Q6"):
    #         # tempDF = tempDF.sort_values('enginev', ascending=False).sort_values('max_powerv', ascending=False)
    #     # 7. Which are the Max Mileage and Max Engine car models?
    #     # if request.GET.get("Q7"):
    #         # tempDF = tempDF.sort_values('mileagev', ascending=False).sort_values('enginev', ascending=False)
    #     # 8. The Best Mileage Car models are?
    #     # if request.GET.get("Q8"):
    #         # tempDF = tempDF.sort_values('mileagev', ascending=False)
    #     if request.method == 'POST':
    #     # if request.POST.get('Q1'):
    #         tempDF = tempDF[tempDF["Q"]==request.GET["Q"]].sort_values('mileagev', ascending=False)
    #         tempDF = tempDF.head()
    #         return render(request, 'selectCar/car.html',{'car':car, "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})
    