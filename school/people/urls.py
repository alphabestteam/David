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
    path('deleteParent/<parent_id>', views.delete_parent, name="Delete Parent"),

    path('connectChild/', views.connect_child_to_parent, name="Connect Child"),
    path('getParentInfo/<parent_id>', views.get_parent_info, name="Get Parent Info"),
    path('getRichChildren/', views.get_rich_children, name="Get Rich Children"),
    path('getParentsFromChild/<child_id>', views.get_parents_from_child, name="Get Parent from Child"),
    path('getChildrenFromParent/<parent_id>', views.get_children_from_parent, name="Get Children From Parents"),
    path('getGrandParents/<person_id>', views.get_grandparents, name="Get Children From Parent"),
    path('getSiblings/<person_id>', views.get_siblings, name="Get Siblings"),

]


