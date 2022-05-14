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
            tempDF = tempDF[tempDF["Brand"]==request.GET["Brand"]].sort_values('selling_price', ascending=False)

        if request.GET.get("year"):
            tempDF = tempDF[tempDF["year"] == int(request.GET["year"])].sort_values('selling_price', ascending=False)

        if request.GET.get("fuel"):
            tempDF = tempDF[tempDF["fuel"]==request.GET["fuel"]].sort_values('mileagev', ascending=False)

        tempDF = tempDF.head()
        # take input data & send to the template
        return render(request, 'selectCar/car.html',{'car':car, "dataY":str(tempDF["selling_price"].values.tolist()), "dataX": str(tempDF["name"].values.tolist())})
    
    def post(self, request):
        # select car & send to the template with the selected car info
        # csvfile = request.FILES['csv_file']
        # data = pd.read_csv(csvfile.name)
        #You can create your custom dataframe here before converting it to html in next line
        # data_html = data.to_html() 
        # context = {'loaded_data': data_html}
        # return render(request, "dataflow/table.html", context)
        
        # In the HTML page, use
        # {{loaded_data | safe}}
        pass