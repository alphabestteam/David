from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Event, EventChat, EventFile
from .serializers import EventSerializer, EventChatSerializer, EventFileSerializer

# Create your views here

@api_view(['GET'])
def get_all_events(request):
    events = Event.objects.all()
    events_serialized = EventSerializer(events, many=True)
    return Response(events_serialized.data)
