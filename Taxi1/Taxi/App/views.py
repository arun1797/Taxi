from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from App.models import DriverModel
from App.models import Trip

# Create your views here.
def Add_trip(request):
    return render(request,"Add_trip.html")

def view_trip(request):
    return render(request,"view_trip.html")


def save_trip(request):
    if request.method == 'POST':
        driver = request.POST.get('driver')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        vehicle_no = request.POST.get('vehicle_no')
        start_kilometer = request.POST.get('start_kilometer')
        end_kilometer = request.POST.get('end_kilometer')
        guest_name = request.POST.get('guest_name')
        
        # Create and save the trip object
        trip = Trip.objects.create(
            driver=driver,
            star_date=start_date,
            end_date=end_date,
            vehicle_no=vehicle_no,
            start_kilometer=start_kilometer,
            end_kilometer=end_kilometer,
            guest_name=guest_name
        )
        trip.save()
        
        # Redirect to a success page or another URL
        return redirect('save_trip')
