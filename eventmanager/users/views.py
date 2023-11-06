from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


# Create your views here.
@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    users_serialized = UserSerializer(users, many=True)
    return Response(users_serialized.data)


@api_view(['POST'])
def create_user(request):
    json_data = request.data
    user_serializer = UserSerializer(data=json_data)
    if user_serializer.is_valid():
        user_serializer.save()
        return Response(user_serializer.data)
    return HttpResponse("Incorrect Format", status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_user(request):
    user_id = request['user_id']
    user = User.objects.get(user_id=user_id)
    user.delete()
    return Response(user)
