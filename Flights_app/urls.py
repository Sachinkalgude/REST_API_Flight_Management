from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [

    # Aircraft.
    path('AircraftDetails/', AircraftDetails.as_view()),
    path('Aircraft_retrive_update_delete/<int:pk>/',
         AircraftUpdateDestroyRetrive.as_view()),

    # Cities.
    path('CitiesDetails/', CitiesDetails.as_view()),
    path('Cities_retrive_update_delete/<int:pk>/',
         CitiesUpdateDestroyRetrive.as_view()),

    # Airport.
    path('AirportDetails/', AirportDetails.as_view()),
    path('Airport_retrive_update_delete/<int:pk>/',
         AirportUpdateDestroyRetrive.as_view()),

    # Flight.
    path('FlightDetails/', FlightDetails.as_view()),
    path('Flight_retrive_update_delete/<int:pk>/',
         FlightUpdateDestroyRetrive.as_view()),

    # Flight_report_view.
    path('Flight_Report_View/', Flight_Report_View.as_view())
]
