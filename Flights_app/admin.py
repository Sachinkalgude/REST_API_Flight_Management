from django.contrib import admin
# Register your models here.
from .models import *


@admin.register(Aircraft)
class Aircraft_Admin(admin.ModelAdmin):
    list_display = ['id', "Aircraft_Model",
                    "Aircraft_serialnumber", "Manufacturer"]


@admin.register(Cities)
class Cities_Admin(admin.ModelAdmin):
    list_display = ["id", "City_Name"]


@admin.register(Airport)
class Airport_Admin(admin.ModelAdmin):
    list_display = ["Airport_Name", "Country", "city_name", "ICAO_Code"]


@admin.register(Flight)
class Flight_Admin(admin.ModelAdmin):
    list_display = ["id", "Flight", "Flight_name", "Flight_Id", "Flight_From",
                    "Flight_To", "Departure_Flight_Time", "Aparture_Flight_Time", "created_on"]
