from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer

# Create your views here.
@api_view(['GET'])
def get_all_chats(request):
    chats = Chat.objects.all()
    chats_serialized = ChatSerializer(chats, many=True)
    return Response(chats_serialized.data)
