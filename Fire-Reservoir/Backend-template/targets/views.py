import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import TargetSerializer


@csrf_exempt
def add_target(request):

    data = json.loads(request.body)
    serialized = TargetSerializer(data=data)
    if serialized.is_valid():
        serialized.save()
        return HttpResponse("<h3>Target added successfully</h3>", 200)
    return HttpResponse("Target didnt meet the requirements", 400)


@csrf_exempt
def update_target(request):
    pass
    # Implement here an update function


def all_targets(request):
    pass
    # Implement here a get all targets function
