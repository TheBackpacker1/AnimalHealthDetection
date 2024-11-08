from django.shortcuts import render
from .models import sensor_data_collection
from django.http import HttpResponse




# Create your views here.



def index(request):
    return HttpResponse("<h1> App is running..</h1>")


def add_data(request):
    records ={
       "temp":"23",
       "pulse":"90",
       "acc":"is moving"


    }  
    
    sensor_data_collection.insert_one(records)
    return HttpResponse("New data is added")



def get_all_data(request):
    sensorData= sensor_data_collection.find()
    return HttpResponse(sensorData)






