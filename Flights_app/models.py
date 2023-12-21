from django.db import models
import re
# Create your models here.


class Aircraft(models.Model):
    Aircraft_Model = models.CharField(max_length=50)
    Aircraft_serialnumber = models.CharField(max_length=50, unique=True)
    Manufacturer = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Aircraft_Model} - {self.Aircraft_serialnumber} - {self.Manufacturer}"


class Cities(models.Model):
    City_Name = models.CharField(max_length=50)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.City_Name}"


class Airport(models.Model):
    Airport_Name = models.CharField(max_length=200, unique=True)
    Country = models.CharField(max_length=100, default='India')
    city_name = models.ForeignKey(Cities, on_delete=models.CASCADE)
    ICAO_Code = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return f"{self.ICAO_Code}"


class Flight(models.Model):
    Flight = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    Flight_name = models.CharField(max_length=200)
    Flight_Id = models.CharField(max_length=200, unique=True)
    Flight_From = models.ForeignKey(
        Cities, on_delete=models.CASCADE, related_name='departures')
    Flight_To = models.ForeignKey(
        Cities, on_delete=models.CASCADE, related_name='arrivals')
    Departure_airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name='departures')
    Arrival_airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name='arrivals')
    Departure_Flight_Time = models.DateTimeField()
    Aparture_Flight_Time = models.DateTimeField()

    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.Flight_Id} - {self.Flight} - {self.Flight_name} - {self.Flight_From} - {self.Flight_To} - {self.Departure_airport} - {self.Arrival_airport} - {self.Departure_Flight_Time} - {self.Aparture_Flight_Time} - {self.created_on}"


# It looks like you are encountering a Django error related to reverse accessor clashes in your models. This issue typically occurs when you have two or more foreign keys pointing to the same model without explicitly specifying a related_name for one or both of them.
