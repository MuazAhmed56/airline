from django.shortcuts import render
from . models import Flight

# Create your views here.
def index(request):
    return render(request,"flights/index.html",{"flights":Flight.objects.all()}) 
# Flight class has a method objects which returns all the instances of the 
# class Flight which happen to be all the flights.