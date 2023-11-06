from django.urls import path
from . import views

urlpatterns = [
    path('getAllUsers/', views.get_all_users),
    path('createUser/', views.create_user),
    path('deleteUser/', views.delete_user),
]