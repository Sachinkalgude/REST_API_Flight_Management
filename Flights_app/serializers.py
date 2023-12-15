from rest_framework import serializers
from django.utils import timezone
# models.
from .models import Cities, Airport, Flight, Aircraft


class AircraftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aircraft
        fields = ['id', 'Aircraft_Model',
                  'Aircraft_serialnumber', 'Manufacturer', 'created_on']

        # read_only_fields = ["id", ]


class CitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cities
        fields = ['City_Name']

        # read_only_fields = ["id", ]


class AirportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airport
        fields = ['Airport_Name', 'Country', 'city_name', 'ICAO_Code']

        # read_only_fields = ["id", ]


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = ['Flight', 'Flight_name', 'Flight_Id', 'Flight_From', 'Flight_To',
                  'Departure_airport', 'Arrival_airport', 'Departure_Flight_Time', 'Aparture_Flight_Time', 'created_on']

        # read_only_fields = ["id", ]

    def validate(self, attrs):
        Departure_Flight_Time = attrs.get('Departure_Flight_Time')
        Aparture_Flight_Time = attrs.get('Aparture_Flight_Time')

        if Departure_Flight_Time < timezone.now():
            raise serializers.ValidationError(
                'depart time should be in the future.')

        if Departure_Flight_Time >= Aparture_Flight_Time:
            raise serializers.ValidationError(
                'Aparture time should be after departure time.')

        if Departure_Flight_Time == Aparture_Flight_Time:
            raise serializers.ValidationError(
                'Departure and Aparture should not be same.')

        return attrs
