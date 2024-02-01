from django.urls import path
from apps.endpoints.views import FlightPredict

urlpatterns = [
    path("api/v1/flight_prediction", FlightPredict, name="flight-predict"),
]
