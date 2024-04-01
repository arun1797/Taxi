from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from App.models import DriverModel
from App.models import Trip

# Create your views here.
def Add_trip(request):
    return render(request,"Add_trip.html")

def view_trip(request):
    return render(request,"view_trip.html")

def register(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")


def register_function(request):
    if request.method == "POST":
        
