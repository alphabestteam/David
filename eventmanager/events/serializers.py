from rest_framework import serializers
from .models import Event, EventChat, EventFile


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventChatSerializer(EventSerializer):
    class Meta:
        model = EventChat
        fields = '__all__'


class EventFileSerializer(EventSerializer):
    class Meta:
        model = EventFile
        fields = '__all__'
