from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model
user=get_user_model()

class DriverModel(models.Model):
    driver=models.ForeignKey(user,on_delete=models.CASCADE)
    age=models.IntegerField()
    phoneno=models.CharField(max_length=10)

class Trip(models.Model):
    driver = models.ForeignKey(DriverModel, on_delete=models.CASCADE)
    trip_number = models.CharField(max_length=10, unique=True)
    star_date=models.DateField()
    end_date=models.DateField()
    vehicle_no=models.TextField()
    start_kilometer=models.TextField()
    end_kilometer=models.TextField()
    guest_name=models.CharField(max_length=100)
    

    def save(self, *args, **kwargs):
        if not self.trip_number:  # If trip number is not set
            last_trip = Trip.objects.order_by('-id').first()  # Get the last trip object
            if last_trip:
                last_trip_number = int(last_trip.trip_number.replace("trp", ""))  # Extract the numeric part
                self.trip_number = "trp" + str(last_trip_number + 1)  # Increment and format
            else:
                self.trip_number = "trp1"  # If it's the first trip
        super().save(*args, **kwargs)

    def __str__(self):
        return self.trip_number
