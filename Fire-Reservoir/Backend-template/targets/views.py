import json

from django.http import QueryDict
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import TargetSerializer
from .models import Target


@csrf_exempt
def add_target(request):
    data = json.loads(request.body)
    serialized = TargetSerializer(data=data)
    if serialized.is_valid():
        serialized.create(data).save()
        return HttpResponse("Target added successfully", status=status.HTTP_201_CREATED)
    return HttpResponse("Target didnt meet the requirements", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def update_target(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        target_id = data["target_id"]
        target = Target.objects.get(target_id=target_id)
        target_serialized = TargetSerializer(target, data=data)
        if target_serialized.is_valid():
            target_serialized.update(target, data).save()
            return HttpResponse("successfully updated the target", status=status.HTTP_200_OK)
        return HttpResponse("Target didnt meet the requirements", status=status.HTTP_400_BAD_REQUEST)


def all_targets(request):
    targets = Target.objects.all()
    targets_data = TargetSerializer(targets, many=True).data
    return JsonResponse(targets_data, safe=False, status=status.HTTP_200_OK)
