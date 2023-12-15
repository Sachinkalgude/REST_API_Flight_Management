from django.urls import path
from .views import *
urlpatterns = [
    path('user_email_register/', user_email_register.as_view())
]
