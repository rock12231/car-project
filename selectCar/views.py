from ast import Str
from asyncio.windows_events import NULL
from copyreg import pickle
from django.shortcuts import render
from django.views import View
import pandas as pd
import plotly.express as px
import json
from .models import ContactUs
import pickle
# Read data from csv file
df = pd.read_csv("selectCar/data/processed_cardekho.csv")

# Current car details
car: dict = {
            'brand': "",
            'year': "",
            'price': "",
            'cars': "",
            'msg': "",
            'dataSet': "",
            'alert': ""
            }

# Class Based rendering the index page
class Home(View):
    
    def get(self, request):
        return render(request, 'selectCar/index.html')

    def post(self, request):
        if request.method == 'POST':
            name = request.POST['name']
            if name.find(' ') != -1:
                first_name, Last_name = name.split(' ', 1)
            else:
                first_name = name
                Last_name = name
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            objects = ContactUs()
            data = ContactUs.objects.create(first_name=first_name, last_name=Last_name, User_email=email, User_subject=subject, User_message=message)
            data.save()
            car['alert'] = "Thankyou for contacting us! Our team will get back to you soon."
        else:
            car['alert'] = "Please fill the form again."
        return render(request, 'selectCar/index.html',{'car':car})
     
# Class Based rendering the Car page
class Car(View):
    
    # Get Function to render the car page
    def get(self, request):
        tempDF = df.copy() 
        tempOptions = tempDF["Brand"].unique()
        car['cars'] = tempOptions
        car['msg'] = ""  
        tempDF = tempDF.head()
        car['dataSet'] = len(tempDF)
        return render(request, 'selectCar/car.html',{"car":car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})
    
    # Post Function to render the car page
    def post(self, request):       
        tempDF = df.copy()
        tempOptions = tempDF["Brand"].unique()
        car['cars'] = tempOptions
        car['msg'] = ""
        
        # If the Brand Year Price is not NULL then assign value to car & Type Cast String to Int
        if request.POST["Brand"]:
            car['brand'] = request.POST["Brand"]
        if request.POST["price"]:
            int_price = int(request.POST["price"])
            car['price'] = int_price
        if request.POST["year"] :
            int_year = int(request.POST["year"])
            car['year'] = int_year
                    
        # Filter the dataframe based Brand Year Price
        if request.POST["Brand"] and request.POST["year"] and len(request.POST["year"])==4 and request.POST["price"] and len(request.POST["price"])>4:
            tempDF = tempDF[(tempDF["Brand"]==request.POST["Brand"]) & (tempDF["year"]==int_year) & (tempDF["selling_price"]<int_price)].sort_values('selling_price', ascending=False)
            print(tempDF,"Brand Year Price..................")
        
        # Filter the dataframe based Brand Year
        elif request.POST["Brand"] and request.POST["year"] and len(request.POST["year"])==4:
            tempDF = tempDF[(tempDF["Brand"]==request.POST["Brand"]) & (tempDF["year"]==int_year)].sort_values('selling_price', ascending=False)
            print(tempDF,"Brand Year....................")
        
        # Filter the dataframe based Brand Price
        elif request.POST["Brand"] and request.POST["price"] and len(request.POST["price"])==4:
            tempDF = tempDF[(tempDF["Brand"]==request.POST["Brand"]) & (tempDF["selling_price"]<int_price)].sort_values('selling_price', ascending=False)
            print(tempDF,"Brand Price....................")
        
        # Filter the dataframe based Year Price
        elif request.POST["year"]  and len(request.POST["year"])==4 and request.POST["price"] and len(request.POST["price"])>4:
            tempDF = tempDF[(tempDF["year"]==int_year) & (tempDF["selling_price"]<int_price)].sort_values('selling_price', ascending=False)
            print(tempDF,"Year Price....................")
        
        # Filter the dataframe based on Brand only
        elif request.POST["Brand"]:
            tempDF = tempDF[tempDF["Brand"]==request.POST["Brand"]].sort_values('selling_price', ascending=False)
            # print(tempDF,"Brand ........")
            
        # Filter the dataframe based on Year only
        elif request.POST["year"] and len(request.POST["year"])==4:
            tempDF = tempDF[tempDF["year"]==int_year].sort_values('selling_price', ascending=False)
            # print(tempDF,"Year ........")
        
        # filter the dataframe based on Price only  
        elif request.POST["price"] and len(request.POST["price"])>4:
            tempDF = tempDF[tempDF["selling_price"]<int_price].sort_values('mileagev', ascending=False)
            # print(tempDF,"Price ........") 
                   
        # Wrong input or invalid input or over the limit input then show the error message
        else :
            car['msg'] = "Please Enter Valid Year and Amount, Like 2018 and Amount between 1,00,000 to 10,00,000."
            tempDF = tempDF.head()
            # print("Wrong Input ........")
        
        # Check the dataframe is empty or not if empty then show the message
        if tempDF.empty:
            car['msg'] = "No Car Found with the given details"
        
        # Collect the dataframe data and sort the head and send to render the car page
        tempDF = tempDF.head()
        car['dataSet'] = len(tempDF)
        return render(request, 'selectCar/car.html',{"car":car, "dataT":tempDF.values.tolist(), "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})
  
# Prediction
class Prediction(View):
    
    def get(self, request):
        return render(request, 'selectCar/prediction.html')
    
    def post(self, request):
        if request.POST["selling_price"]:
            selling_price = int(request.POST["selling_price"])
            print(selling_price)
        
        if request.POST["km_driven"]:
            km_driven = int(request.POST["km_driven"])
            print(km_driven)
            
        if request.POST["transmission"]:
            transmission = int(request.POST["transmission"])
            print(transmission)
            
        if request.POST["owner"]:
            owner = int(request.POST["owner"])
            print(owner)
            
        if request.POST["mileage"]:
            mileage = float(request.POST["mileage"])
            print(mileage)
            
        if request.POST["engine"]:
            engine = int(request.POST["engine"])
            print(engine)
            
        if request.POST["max_power"]:
            max_power = int(request.POST["max_power"])
            print(max_power)
            
        if request.POST["brand"]:
            brand = int(request.POST["brand"])
            print(brand)
	    
        UserInput = []
        model = pickle.load('selectCar/data/deepmodel.sav')
        UserInput.append(km_driven)
        UserInput.append(transmission)
        UserInput.append(owner)
        UserInput.append(mileage)
        UserInput.append(engine)
        UserInput.append(max_power)
        UserInput.append(brand)
        result = model.predict([UserInput])
        return render(request, 'selectCar/prediction.html',{'result':result})

  

    
    
    # """ --->> Function basded rendering car page with dynamic data & plot Chart.JS Graph and Datatable <<--- """ #

# 1. Which is the Best Mileage Car  
def data1(request):
    tempDF = df.copy()
    tempDF = tempDF.sort_values('mileagev', ascending=False)
    tempDF = tempDF.head()
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
