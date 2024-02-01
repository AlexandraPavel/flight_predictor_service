from django.db import models

class Endpoint(models.Model):

    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

class Flight(models.Model):
    
    DEPARTURE_CHOICES = (
        ('Bucuresti', 'Bucuresti'),
        ('Iasi', 'Iasi'),
        ('Cluj', 'Cluj'),
    )

    DESTINATION_CHOICES = (
        ('Istanbul', 'Istanbul'),
        ('Londra', 'Londra'),
        ('Paris', 'Paris'),
        ('Amsterdam', 'Amsterdam'),
        ('Madrid', 'Madrid'),
        ('Frankfurt', 'Frankfurt'),
        ('Barcelona', 'Barcelona'),
        ('Munich', 'Munich'),
        ('Roma', 'Roma'),
        ('Lisabona', 'Lisabona'),
        ('Dublin', 'Dublin'),
        ('Viena', 'Viena'),
        ('Manchester', 'Manchester'),
        ('Atena', 'Atena'),
        ('Zurich', 'Zurich'),
        ('Oslo', 'Oslo'),
        ('Copenhaga', 'Copenhaga'),
        ('Milano', 'Milano'),
        ('Berlin', 'Berlin'),
        ('Bruxelles', 'Bruxelles'),
    )

    departure = models.CharField(max_length=128, blank = False, null = False, choices = DEPARTURE_CHOICES)
    destination = models.CharField(max_length=128, blank = False, null = False, choices = DESTINATION_CHOICES)
    flight_date = models.DateField(blank = False, null = False)
    arrival_date = models.DateField(blank=False, null = False)
