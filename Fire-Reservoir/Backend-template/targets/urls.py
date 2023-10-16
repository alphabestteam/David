from django.urls import path
from . import views

urlpatterns = [
    path('AddTarget/', views.add_target, name="add target"),
]
