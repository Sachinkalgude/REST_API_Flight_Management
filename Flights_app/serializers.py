from rest_framework import serializers
from django.utils import timezone
# models.
from .models import Cities, Airport, Flight, Aircraft
from django.db.models import Q
from django.db.models import F, Sum, Avg, Max
from datetime import datetime, timedelta


class AircraftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aircraft
        fields = ['id', 'Aircraft_Model',
                  'Aircraft_serialnumber', 'Manufacturer', 'created_on']

        read_only_fields = ["id", ]

    def validate(self, attrs):
        Aircraft_serial_number = attrs.get('Aircraft_serialnumber')
        Manufactur_er = attrs.get('Manufacturer')

        if Aircraft.objects.filter(Q(Aircraft_serialnumber=Aircraft_serial_number) & Q(Manufacturer=Manufactur_er)):
            raise serializers.ValidationError({
                'data_exist': 'Entered Aircraft Details Already Exist.'
            })

        return attrs


class CitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cities
        fields = ['City_Name']

        read_only_fields = ["id", ]

    def validate(self, attrs):
        city_name = attrs.get('City_name')

        if city_name == None:
            raise serializers.ValidationError({
                'required': 'city name is required.'
            })

        if city_name.isdigit():
            raise serializers.ValidationError(
                'Digits not allowed in city name.')

        return attrs


class AirportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airport
        fields = ['Airport_Name', 'Country', 'city_name', 'ICAO_Code']

        read_only_fields = ["id", ]

    def validate(self, attrs):
        ICAO_Code = attrs.get('ICAO_Code')
        Country = attrs.get('Country')

        if len(ICAO_Code) >= 4 or ICAO_Code.isdigit():
            raise serializers.ValidationError(
                'ICAO_Code length is not more than 4 and digit is not allowed.')

        if Country != 'India':
            raise serializers.ValidationError(
                'Country should be India not others.')

        return attrs


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = ['Flight', 'Flight_name', 'Flight_Id', 'Flight_From', 'Flight_To',
                  'Departure_airport', 'Arrival_airport', 'Departure_Flight_Time', 'Aparture_Flight_Time', 'created_on']

        read_only_fields = ["id", ]

    def validate(self, attrs):
        Departure_Flight_Time = attrs.get('Departure_Flight_Time')
        Aparture_Flight_Time = attrs.get('Aparture_Flight_Time')
        flight_ = attrs.get('Flight')
        Flight_id = attrs.get('Flight_Id')
        Departure_airport = attrs.get('Departure_airport')
        Arrival_airport = attrs.get('Arrival_airport')

        if Flight.objects.filter(Q(Flight=flight_) & Q(Flight_id=Flight_id)):
            raise serializers.ValidationError({
                'flight_assigned': 'This Flight already has been assigned.'
            })

        if not Departure_Flight_Time and not Aparture_Flight_Time:
            pass
        if Departure_Flight_Time and Aparture_Flight_Time:
            if Departure_Flight_Time < timezone.now():
                raise serializers.ValidationError(
                    'depart time should be in the future.')

            if Departure_Flight_Time >= Aparture_Flight_Time:
                raise serializers.ValidationError(
                    'Aparture time should be after departure time.')

            if Departure_Flight_Time == Aparture_Flight_Time:
                raise serializers.ValidationError(
                    'Departure and Aparture should not be same.')

        if Flight.objects.filter(Q(Flight=flight_)):
            if not Departure_Flight_Time and not Aparture_Flight_Time:
                pass
            else:
                aparture_time = Flight.objects.filter(Q(Flight=flight_) & Q(
                    is_active=True)).aggregate(apartime=Max('Aparture_Flight_Time'))
                print(aparture_time)

                Apartime = aparture_time['apartime'] + timedelta(minutes=20)
                print(Apartime)

                if Departure_Flight_Time < Apartime:
                    raise serializers.ValidationError({
                        "flight_time": "You should enter departure time after 20 Minutes's arrive time."
                    })

                dep_center = Flight.objects.filter(Q(Flight=flight_) & Q(
                    Aparture_Flight_Time=aparture_time['apartime'])).values('Arrival_airport')
                print(dep_center)

                if int(Departure_airport.id) != dep_center[0]['Arrival_airport']:
                    raise serializers.ValidationError({
                        "flight_arrival": "This flight should be departure from arrival destination."
                    })

        return attrs
