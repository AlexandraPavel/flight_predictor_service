from django.urls import path
from apps.endpoints.views import FlightView

urlpatterns = [
    path("api/v1/flight", FlightView, name="flight-view"),
]
