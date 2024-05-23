from apps.endpoints.models import MLAlgorithm

from apps.endpoints.models import MLRequest

import json
from numpy.random import rand
from rest_framework import views, status
from rest_framework.response import Response

from server.wsgi import registry


from django.db.models import F
import datetime


from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from datetime import datetime

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

@api_view(('GET','POST'))
def FlightPredict(request):
    if request.method !='POST':
        return Response({"status": "not good"})

    if request.method =='POST':
        form = request.POST
        print("Form", form)
        algorithm_status = "production"
        algorithm_version = None
        endpoint_name = "flight"

        algs = MLAlgorithm.objects.filter(parent_endpoint__name = endpoint_name, status__status = algorithm_status, status__active=True)

        if algorithm_version is not None:
            algs = algs.filter(version = algorithm_version)
        message = ''+endpoint_name + " " + str(list(algs))

        if len(algs) == 0:
            print("Eroarea 1")
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        if len(algs) != 1:
            print("Eroarea 2")
            return Response(
                {"status": "Error", "message": message + "There are muliple models"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        alg_index = 0
        algorithm_object = registry.endpoints[algs[alg_index].id]
        prediction = algorithm_object.compute_prediction(form)

        label = prediction["label"] if "label" in prediction else "error"
        ml_request = MLRequest(
            input_data=json.dumps(form),
            full_response=prediction,
            response=label,
            feedback="",
            parent_mlalgorithm=algs[alg_index],
        )
        ml_request.save()

        prediction["request_id"] = ml_request.id

        return Response({"data": prediction})
