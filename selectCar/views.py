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
            'cars':"",
            'msg':""
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
        
        if request.POST["Brand"]:
            tempDF = tempDF[tempDF["Brand"]==request.POST["Brand"]].sort_values('selling_price', ascending=False)
            tempDF = tempDF.head()
            
        if request.POST["year"] and len(request.POST["year"])==4:
            print("Y................................")
            int_year = int(request.POST["year"])
            tempDF = tempDF[tempDF["year"]==int_year].sort_values('selling_price', ascending=False)
            tempDF = tempDF.head()
            
        if request.POST["price"] and len(request.POST["price"])>4:
            print("P................................")
            int_price = int(request.POST["price"])
            tempDF = tempDF[tempDF["selling_price"]<int_price].sort_values('mileagev', ascending=False)
            tempDF = tempDF.head()
            
        else :
            car['msg'] = "Please Enter Valid Year and Amount, Like 2018 and Amount between 1,00,000 to 10,00,000."
            tempDF = tempDF.head()
        
        return render(request, 'selectCar/car.html',{"car":car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})
    
# 1. Which is the Best Mileage Car  
def data1(request):
    tempDF = df.copy()
    tempDF = tempDF.sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

# 2. Car's showcased according to the Selling Price Range (Min)
def data2(request):
    tempDF = df.copy()
    tempDF = tempDF[(tempDF["mileagev"]>=400000)].sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

# 2. Car's showcased according to the Selling Price Range (Max)
def data3(request):
    tempDF = df.copy()
    tempDF = tempDF[(tempDF["mileagev"]<=800000)].sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})


# 3. The Highest Selling Price cars?
def data4(request):
    tempDF = df.copy()
    tempDF = tempDF.sort_values('selling_price', ascending=False).head()
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})


# 4. Which are the High Power and Low Selling Price car models?
def data5(request):
    tempDF = df.copy()
    tempDF = tempDF.sort_values('selling_price', ascending=True).head()
    tempDF = df.sort_values('max_powerv', ascending=False).head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

# 5. Which are the Max Mileage and Max Power car models?
def data6(request):
    tempDF = df.copy()
    tempDF = df.sort_values('mileagev', ascending=False).head()
    tempDF=  df.sort_values('max_powerv', ascending=False).head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})


# 6. Which are the Max Engine and Max Power car models?
def data7(request):
    tempDF = df.copy()
    tempDF = tempDF.sort_values('enginev', ascending=False).head()
    tempDF=  tempDF.sort_values('max_powerv', ascending=False).head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

# 7. Which are the Max Mileage and Max Engine car models?
def data8(request):
    tempDF = df.copy()
    tempDF = tempDF.sort_values('mileagev', ascending=False).head()
    tempDF=  tempDF.sort_values('enginev', ascending=False).head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

# 8. The Best Mileage Car models are?
def data9(request):
    tempDF = df.copy()
    tempDF = tempDF.sort_values('mileagev', ascending=False).head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})



        
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
    