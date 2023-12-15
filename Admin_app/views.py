from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.generics import ListCreateAPIView
# Create your views here.


class user_email_register(ListCreateAPIView):
    serializer_class = userSerializer
    queryset = user.objects.all()
