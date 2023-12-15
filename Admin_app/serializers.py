from rest_framework import serializers
from .models import *


class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = user
        fields = ['id', 'first_name', 'middel_name',
                  'last_name', 'email', 'phone_number']
