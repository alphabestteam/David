from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.get_all_chats),
]