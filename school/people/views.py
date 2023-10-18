import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Person, Parent
from .serializers import PersonSerializer, ParentSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

'''Person API Functions'''


@csrf_exempt
def get_all_people(request):
    if request.method == "GET":
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
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


'''Parent API Functions'''


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


@csrf_exempt
def get_rich_children(request):
    if request.method == "GET":
        rich_parents = Parent.objects.filter(salary__gtea=50000)
        rich_children = ParentSerializer(rich_parents).data["children"]
        print(rich_children)
        for child_id in rich_children:
            child = Person.objects.get(id=child_id)
            child_age = datetime.datetime.now().year - child.birth_date.year
            if child_age < 18:
                rich_children.remove(child_id)
        return JsonResponse({"Rich Children": rich_children}, safe=False, status=status.HTTP_200_OK)

# @csrf_exempt
# def
