from ast import Str
from django.shortcuts import render
from django.views import View
import pandas as pd
import plotly.express as px
import json

# Read data from csv file
df = pd.read_csv("selectCar/data/processed_cardekho.csv")

# Current car details
car: dict = {
            'car_name': "",
            'car_model': "",
            'car_year': "",
            'car_price': "",
            'brand': "",
            'year': "",
            'cars': "",
            'msg': ""
            }

# Class Based rendering the index page
class Home(View):
    def get(self, request):
        return render(request, 'selectCar/index.html')

# Class Based rendering the Car page
class Car(View):
    
    # Get Function to render the car page
    def get(self, request):
        tempDF = df.copy() 
        tempOptions = tempDF["Brand"].unique()
        car['cars'] = tempOptions  
        tempDF = tempDF.head()
        # data = tempDF.to_dict(orient='records')
        # for i in data[0]:
        #     print(i,".......")
            # car['car_name'] = i.car_name,
            # car['car_model'] = i.car_model,
            # car['car_year'] = i.car_year,
            # car['car_price'] = i.car_price,
        # for i in range(len(data)):
            # if len(data) == i:
                # car['car_name'] = list(data[i])
            # if len(data) == 2:
                # car['car_year'] = list(data[i])
            # if data.index(i) == 3:
                # car['car_price'] = list(data[i])
            # if data.index(i) == 15:
                # car['car_model'] = list(data[i])
        # print(data[0],"........................")
        return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})
    
    # Post Function to render the car page
    def post(self, request):       
        tempDF = df.copy()
        tempOptions = tempDF["Brand"].unique()
        car['cars'] = tempOptions
        
        # Filter the dataframe based on the selected car
        if request.POST["Brand"]:
            tempDF = tempDF[tempDF["Brand"]==request.POST["Brand"]].sort_values('selling_price', ascending=False)
            tempDF = tempDF.head()
            
        # Filter the dataframe based on the selected year
        if request.POST["year"] and len(request.POST["year"])==4:
            int_year = int(request.POST["year"])
            tempDF = tempDF[tempDF["year"]==int_year].sort_values('selling_price', ascending=False)
            tempDF = tempDF.head()
        
        # filter the dataframe based on the selected Price  
        if request.POST["price"] and len(request.POST["price"])>4:
            int_price = int(request.POST["price"])
            tempDF = tempDF[tempDF["selling_price"]<int_price].sort_values('mileagev', ascending=False)
            tempDF = tempDF.head()
        
        # Wrong input message
        else :
            car['msg'] = "Please Enter Valid Year and Amount, Like 2018 and Amount between 1,00,000 to 10,00,000."
            tempDF = tempDF.head()
            
        return render(request, 'selectCar/car.html',{"car":car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})
  
    
""" --->> Function basded rendering car page with dynamic data & pot Chart.JS Graph and Datatable <<--- """

# 1. Which is the Best Mileage Car  
def data1(request):
    tempDF = df.copy()
    tempDF = tempDF.sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    car_data(tempDF)
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

# 2. Car's showcased according to the Selling Price Range (Min)
def data2(request):
    tempDF = df.copy()
    tempDF = tempDF[(tempDF["selling_price"]>=400000)].sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

# 3. Car's showcased according to the Selling Price Range (Max)
def data3(request):
    tempDF = df.copy()
    tempDF = tempDF[(tempDF["selling_price"]<=800000)].sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})


# 4. The Highest Selling Price cars?
def data4(request):
    tempDF = df.copy()
    tempDF = tempDF.sort_values('selling_price', ascending=False).head()
    tempDF = tempDF.head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})


# 5. Which are the High Power and Low Selling Price car models?
def data5(request):
    tempDF = df.copy()
    tempDF = tempDF.sort_values('selling_price', ascending=True).head()
    tempDF = df.sort_values('max_powerv', ascending=False).head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

# 6. Which are the Max Mileage and Max Power car models?
def data6(request):
    tempDF = df.copy()
    tempDF = df.sort_values('mileagev', ascending=False).head()
    tempDF=  df.sort_values('max_powerv', ascending=False).head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})


# 7. Which are the Max Engine and Max Power car models?
def data7(request):
    tempDF = df.copy()
    tempDF = tempDF.sort_values('enginev', ascending=False).head()
    tempDF=  tempDF.sort_values('max_powerv', ascending=False).head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

# 8. Which are the Max Mileage and Max Engine car models?
def data8(request):
    tempDF = df.copy()
    tempDF = tempDF.sort_values('mileagev', ascending=False).head()
    tempDF=  tempDF.sort_values('enginev', ascending=False).head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

# 9. The Best Mileage Car models are?
def data9(request):
    tempDF = df.copy()
    tempDF = tempDF.sort_values('mileagev', ascending=False).head()
    return render(request, 'selectCar/car.html',{'car':car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})

def car_data(tempDF):
    data = tempDF.to_dict(orient='records')
    for i in data[0]:
        print(i,".......")
        # car['car_name'] = i.car_name,
        # car['car_model'] = i.car_model,
        # car['car_year'] = i.car_year,
        # car['car_price'] = i.car_price,