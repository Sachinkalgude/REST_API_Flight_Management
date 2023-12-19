from rest_framework import status
from django.shortcuts import render
from .serializers import *
from .models import *
from django.utils import timezone
import requests


# generic_api.
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

# permissions
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

# simple_jwt_authentication
from rest_framework_simplejwt.authentication import JWTAuthentication

# filter search.
from rest_framework.filters import SearchFilter

# apiview
from rest_framework.views import APIView
from rest_framework import response
from rest_framework.response import Response

# Q object.
from django.db.models import Q

# status
from rest_framework import generics, status


class AircraftDetails(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class AircraftUpdateDestroyRetrive(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class CitiesDetails(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class CitiesUpdateDestroyRetrive(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class AirportDetails(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirportUpdateDestroyRetrive(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class FlightDetails(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Flight.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['Departure_airport__ICAO_Code',
                     'Arrival_airport__ICAO_Code']
    serializer_class = FlightSerializer


class FlightUpdateDestroyRetrive(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Flight.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['Departure_airport__ICAO_Code',
                     'Arrival_airport__ICAO_Code']
    serializer_class = FlightSerializer


class Flight_Report_View(APIView):
    serializer_class = FlightSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        Departure_datetime = request.query_params.get(
            'Departure_Flight_Time')
        Aparture_datetime = request.query_params.get(
            'Aparture_Flight_Time')

        try:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            queryset = (
                Flight.objects.select_related('Flight', 'Departure_airport').filter(Q(Departure_Flight_Time__gte=Departure_datetime) & Q(
                    Aparture_Flight_Time__lte=Aparture_datetime)).order_by('Departure_airport')
            )
            print(queryset)
        except ValueError:
            return Response(
                'invalid parameters', status=status.HTTP_400_BAD_REQUEST
            )

        data = {}
        for flight in queryset:
            if not data.__contains__(flight.Departure_airport.ICAO_Code):
                flight_time_for_each_aircraft = []
                data[flight.Departure_airport.ICAO_Code] = {
                    'airport_name': flight.Departure_airport.Airport_Name,
                    'flights_count': 0,
                    'flight_time_for_each_aircraft': flight_time_for_each_aircraft,
                }
            data[flight.Departure_airport.ICAO_Code]['flights_count'] += 1
            flight_time_for_each_aircraft.append(
                {
                    'aircraft': AircraftSerializer(flight.Flight).data,
                    'flight_time': '{} minutes'.format(
                        (flight.Aparture_Flight_Time -
                         flight.Departure_Flight_Time).total_seconds()/60
                    ),
                }
            )

        response = {
            'status': 1,
            'message': 'successfully retrived flights',
            'data': {Departure_datetime, Aparture_datetime},
        }

        response['data'] = data
        return Response(response)

# try just.


# search with modelrelationship solution.thursday.
# When you're working with a ForeignKey field and you want to perform a search based on a related model's field in Django REST Framework, you need to reference the related model's field in the search_fields using a double underscore (__).

# In your case, if Departure_airport is a ForeignKey to the Aircraft model, and you want to search based on the manufacturer field of the related Aircraft, you should use the following:

# python
# Copy code
# # Assuming your Flight model looks like this:
# class Flight(models.Model):
#     Departure_airport = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
#     # Other fields...

# # Your FlightDetails view can be modified like this:
# class FlightDetails(ListCreateAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [AllowAny]
#     queryset = Flight.objects.all()
#     filter_backends = [SearchFilter]
#     search_fields = ['Departure_airport__manufacturer']  # Use double underscore to reference related model's field
#     serializer_class = FlightSerializer
# Make sure to use the correct field names based on your actual models.

# This modification should allow you to perform a search based on the manufacturer field of the related Aircraft model in your FlightDetails view. Adjust the field names as needed for your specific models and relationships.


# imp.

# class MyApiView(APIView):
#     def get(self, request, format=None):
#         # Accessing request.GET parameters
#         param_value = request.GET.get('param_name', default_value)

#         # Accessing request.POST parameters
#         post_param_value = request.data.get('post_param_name', default_value)

#         # Accessing request headers
#         header_value = request.headers.get('Header-Name', default_value)

#         # Accessing user information
#         user = request.user
#         user_id = user.id

#         # Your view logic here...

#         return Response({'message': 'Response message'}, status=status.HTTP_200_OK)
