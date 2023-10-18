import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Person, Parent
from .serializers import PersonSerializer, ParentSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

'''
Person API Functions
'''


@csrf_exempt
def get_all_people(request):
    if request.method == "GET":
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    return HttpResponse("Incorrect method type", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def add_person(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serialized = PersonSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return HttpResponse("Person was successfully added to the DB", status=status.HTTP_201_CREATED)
        return HttpResponse("Person didnt meet the requirements", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def delete_person(request, person_id):
    if request.method == "DELETE":
        try:
            person = Person.objects.get(id=person_id)
            person.delete()
            return HttpResponse(f"Successfully deleted person with ID: {person_id}", status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return HttpResponse(f"That ID does not exist", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def update_person(request):
    if request.method == "PUT":
        data = JSONParser().parse(request)
        person_id = data["id"]
        try:
            person = Person.objects.get(id=person_id)
        except ObjectDoesNotExist:
            return HttpResponse(f"That person does not exist", status=status.HTTP_400_BAD_REQUEST)
        serialized = PersonSerializer(person, data=data)
        if serialized.is_valid():
            serialized.update(person, data)
            return HttpResponse("Successfully updated the person", status=status.HTTP_200_OK)
        return HttpResponse("Error: Updated details for person dont meet the requirements",
                            status=status.HTTP_400_BAD_REQUEST)


'''
Parent API Functions
'''


@csrf_exempt
def get_all_parents(request):
    if request.method == "GET":
        parent = Parent.objects.all()
        serializer = ParentSerializer(parent, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


@csrf_exempt
def add_parent(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serialized = ParentSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return HttpResponse("Parent was successfully added to the DB", status=status.HTTP_201_CREATED)
        return HttpResponse("Parent didnt meet the requirements", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def delete_parent(request, parent_id):
    if request.method == "DELETE":
        try:
            parent = Parent.objects.get(id=parent_id)
            parent.delete()
            return HttpResponse(f"Successfully deleted Parent with ID: {parent_id}", status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return HttpResponse(f"That ID does not exist", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def update_parent(request):
    if request.method == "PUT":
        data = JSONParser().parse(request)
        parent_id = data["id"]
        try:
            parent = Parent.objects.get(id=parent_id)
        except ObjectDoesNotExist:
            return HttpResponse(f"That parent does not exist", status=status.HTTP_400_BAD_REQUEST)
        serialized = ParentSerializer(parent, data=data)
        if serialized.is_valid():
            serialized.save()
            return HttpResponse("Successfully updated the parent", status=status.HTTP_200_OK)
        return HttpResponse("Error: the updated details for parent dont meet the requirements",
                            status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def connect_child_to_parent(request):
    if request.method == "PUT":
        data = JSONParser().parse(request)
        parent_id = data["parent_id"]
        child_id = data["child_id"]
        try:
            parent = Parent.objects.get(id=parent_id)
            child = Person.objects.get(id=child_id)
        except ObjectDoesNotExist:
            return HttpResponse("The child or parent doesnt exist", status=status.HTTP_400_BAD_REQUEST)
        parent.children.add(child)
        return HttpResponse("Successfully added the child to the parent", status=status.HTTP_201_CREATED)
    return HttpResponse(f"Error: Received method type {request.method} instead of method type PUT",
                        status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def get_parent_info(request, parent_id):
    if request.method == "GET":
        try:
            parent = Parent.objects.get(id=parent_id)
            parent_data = ParentSerializer(parent).data
            children_id = parent_data["children"]
            children = []
            for child_id in children_id:
                child = Person.objects.get(id=child_id)
                child_data = PersonSerializer(child).data
                children.append(child_data)
        except ObjectDoesNotExist:
            return HttpResponse("Error: That Parent doesnt exist", status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({"Parent": parent_data, "Children": children}, safe=False, status=status.HTTP_200_OK)
    return HttpResponse(f"Error: Received method type {request.method} instead of method type PUT",
                        status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def get_rich_children(request):
    if request.method == "GET":
        cutoff_age = datetime.datetime.now().year - 18
        rich_children_query = Person.objects.filter(Q(parents__salary__gte=50000) & Q(birth_date__year__lte=cutoff_age))
        rich_children_data = [PersonSerializer(rich_child).data for rich_child in rich_children_query]

        return JsonResponse({"Rich Children": rich_children_data}, safe=False, status=status.HTTP_200_OK)
    return HttpResponse(f"Error: Received method type {request.method} instead of method type PUT",
                        status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def get_parents_from_child(request, child_id):
    if request.method == "GET":
        try:
            child = Person.objects.get(id=child_id)
        except ObjectDoesNotExist:
            return HttpResponse("Error: That ID does not exist", status=status.HTTP_400_BAD_REQUEST)
        # Without serializer
        # parents = ParentSerializer(child.parents.all(), many=True).data
        # return JsonResponse({"Parents": parents}, safe=False, status=status.HTTP_200_OK)

        # With Serializer
        parents = PersonSerializer().get_parents(child)
        return JsonResponse({"Parents": parents}, safe=False, status=status.HTTP_200_OK)

    return HttpResponse(f"Error: Received method type {request.method} instead of method type PUT",
                        status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def get_children_from_parent(request, parent_id):
    if request.method == "GET":
        try:
            parent = Parent.objects.get(id=parent_id)
        except ObjectDoesNotExist:
            return HttpResponse("Error: That ID does not exist", status=status.HTTP_400_BAD_REQUEST)

        children = PersonSerializer(parent.children.all(), many=True).data
        return JsonResponse({"Children": children}, safe=False, status=status.HTTP_200_OK)
    return HttpResponse(f"Error: Received method type {request.method} instead of method type PUT",
                        status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def get_grandparents(request, person_id):
    if request.method == "GET":
        try:
            person = Person.objects.get(id=person_id)
        except ObjectDoesNotExist:
            return HttpResponse("Error: That ID does not exist", status=status.HTTP_400_BAD_REQUEST)
        grandparents = []
        for parent in person.parents.all():
            for grandparent in parent.parents.all():
                grandparents.append(grandparent)
        grandparents_data = ParentSerializer(grandparents, many=True).data
        return JsonResponse({"GrandParents": grandparents_data}, safe=False, status=200)
    return HttpResponse(f"Error: Received method type {request.method} instead of method type PUT",
                        status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def get_siblings(request, person_id):
    if request.method == "GET":
        try:
            person = Person.objects.get(id=person_id)
        except ObjectDoesNotExist:
            return HttpResponse("Error: That ID does not exist", status=status.HTTP_400_BAD_REQUEST)
        siblings = []
        for parent in person.parents.all():
            for sibling in parent.children.all():
                if sibling != person:
                    siblings.append(sibling)
        siblings_data = PersonSerializer(siblings, many=True).data
        return JsonResponse({"Siblings": siblings_data}, safe=False, status=200)
    return HttpResponse(f"Error: Received method type {request.method} instead of method type PUT",
                        status=status.HTTP_400_BAD_REQUEST)