from django.urls import path
from . import views

urlpatterns = [
    path('AddTarget/', views.add_target, name="add target"),
    path('AllTargets/', views.all_targets, name="all target"),
    path('UpdateTarget/', views.update_target, name="update target"),
]
