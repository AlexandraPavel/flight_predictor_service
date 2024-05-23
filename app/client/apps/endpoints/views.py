import json
from numpy.random import rand
from rest_framework import views, status
from rest_framework.response import Response

from apps.endpoints.forms import FlightForm

from django.db.models import F
import datetime


from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
import requests
from rest_framework.renderers import TemplateHTMLRenderer
from apps.endpoints.forms import FlightForm
from datetime import datetime

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

@api_view(('GET','POST'))
def FlightView(request):
    if request.method !='POST':
        form = FlightForm(None)
        response = ''
        return render(request, "flight_page.html", {'form': form, 'response': response})

    if request.method =='POST':
        form = FlightForm(request.POST)
    
        if form.is_valid():

            input_date = datetime.strptime(str(form.cleaned_data["flight_date"]), '%Y-%m-%d')
            form.cleaned_data["flight_date"] = input_date.strftime('%d-%m-%Y')
            input_date = datetime.strptime(str(form.cleaned_data["arrival_date"]), '%Y-%m-%d')
            form.cleaned_data["arrival_date"] = input_date.strftime('%d-%m-%Y')

            res = requests.post("http://127.0.0.1:8080/api/v1/flight_prediction", data=form.cleaned_data)
            
            prediction = res.json()
            
            return render(request, "flight_page.html", {'form': form, 'response': prediction['data']})
        return Response({"status": "not good"})
