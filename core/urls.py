from .views import *
from django.urls import path
urlpatterns = [
    path('phone_search/', serarch_phone),
]