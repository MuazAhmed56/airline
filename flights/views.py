from django.shortcuts import render
from .models import Flight, Passanger
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,"flights/index.html",{"flights":Flight.objects.all()}) 
# Flight class has a method objects which returns all the instances of the 
# class Flight which happen to be all the flights.
def flight(request,flight_id):
    flight=Flight.objects.get(pk=flight_id)
    #print(Flight.objects.get(pk=flight_id).origin) # for debugging
    #print(Flight.objects.get(pk=flight_id).destination) # for debugging
    return render(request,"flights/flights.html", {"flights": flight,
    "passangers":flight.passangers.all(),
    "non_passangers":Passanger.objects.exclude(flights=flight).all()})

def book(request,flight_id):
    if request.method=="POST":
        flight=Flight.objects.get(pk=flight_id)
        passanger=Passanger.objects.get(pk=int(request.POST["passengers"]))
        
        passanger.flights.add(flight)  #adding a new row in the table
        return HttpResponseRedirect(reverse("flight",args=(flight.id,)))