from django.urls import path
from .views import worker_list, worker_detail

urlpatterns = [
    path('workers', worker_list),
    path('workers/<int:pk>', worker_detail),
]
