from django.urls import path
from . import views


urlpatterns = [
    path('getAllPeople/', views.get_all_people, name="Get All People"),
    path('addPerson/', views.add_person, name="Add Person"),
    path('updatePerson/', views.update_person, name="Update Person"),
    path('deletePerson/', views.delete_person, name="Delete Person")
]
