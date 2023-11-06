from django.urls import path
from . import views

urlpatterns = [
    path('event/', views.get_all_events),
]
