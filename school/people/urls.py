from django.urls import path
from . import views


urlpatterns = [
    # People Related
    path('getAllPeople/', views.get_all_people, name="Get All People"),
    path('addPerson/', views.add_person, name="Add Person"),
    path('updatePerson/', views.update_person, name="Update Person"),
    path('deletePerson/<person_id>', views.delete_person, name="Delete Person"),

    # Parent Related
    path('getAllParents/', views.get_all_parents, name="Get All Parents"),
    path('addParent/', views.add_parent, name="Add Parent"),
    path('updateParent/', views.update_parent, name="Update Parent"),
    path('deleteParent/', views.delete_parent, name="Delete Parent"),

    path('connectChild/', views.connect_child_to_parent, name="Connect Child"),
    path('getParentInfo/<parent_id>', views.get_parent_info, name="Get Parent Info"),
    path('getRichChildren/', views.get_rich_children, name="Get Parent Info")

]


