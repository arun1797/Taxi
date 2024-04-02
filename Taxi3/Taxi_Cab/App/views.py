import re
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from App.models import DriverModel
from App.models import Trip
from django.contrib import messages

# Create your views here.
def Add_trip(request):
    drv=DriverModel.objects.all()
    return render(request,"Add_trip.html",{"drv":drv})

def view_trip(request):
    return render(request,"view_trip.html")

def register(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

def register_function(request):
    if request.method == "POST":
        firstname=request.POST.get("fname")
        lastname=request.POST.get("lname")
        phno=request.POST.get("num")
        username=request.POST.get("uname")
        password=request.POST.get("pass")
        if User.objects.filter(username=username).exists():
            messages.info(request,"UserName is Alerdy Exist")
            return redirect("login")
        else:
            u=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,password=password)
            u.save()
            users=u.id
            d=DriverModel(phoneno=phno,driver_id=users)
            d.save()
            return redirect(login)


def login_function(request):
    if request.method == "POST":
        username=request.POST.get("uname")
        password=request.POST.get("pass")
        use=auth.authenticate(username=username,password=password)
        if use is not None:
            auth.login(request,use)
            request.session['uid']=use.id
            return redirect("Add_trip")
        else:
            messages.info(request,"Invalid Username Password")
            return redirect("login")

    else:
        return redirect("login")

def logout(request):
    auth.logout(request)
    return redirect("login")


def add_trip_function(request):
    if request.method == 'POST':
        sel = request.POST.get('sel')
        starting_place = request.POST.get('starting_place')
        ending_place = request.POST.get('ending_place')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        vehicle_name = request.POST.get('vehicle_name')
        vehicle_no = request.POST.get('vehicle_no')
        start_kilometer = request.POST.get('start_kilometer')
        end_kilometer = request.POST.get('end_kilometer')
        toll_charge = request.POST.get('toll_charge')
        parking_charge = request.POST.get('parking_charge')
        guest_name = request.POST.get('guest_name')

        drive = DriverModel.objects.get(id=sel)

        trip = Trip(
            driver=drive,
            start_place=starting_place,
            end_place=ending_place,
            star_date=start_date,
            end_date=end_date,
            vehicle_name=vehicle_name,
            vehicle_no=vehicle_no,
            start_kilometer=start_kilometer,
            end_kilometer=end_kilometer,
            toll=toll_charge,
            parking=parking_charge,
            guest_name=guest_name,
        )
        trip.save()

        # Redirect to a success page or any other page
        return redirect('Add_trip')

    # Render the form template if it's a GET request
    return redirect("Add_trip")



