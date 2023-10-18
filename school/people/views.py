from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Person
from .serializers import PersonSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status


# Create your views here.
@csrf_exempt
def get_all_people(request):
    if request.method == "GET":
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


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
            serialized.update()
            return HttpResponse("Successfully updated the person", status=status.HTTP_200_OK)
        return HttpResponse("Error: Updated details for person dont meet the requirements",
                            status=status.HTTP_400_BAD_REQUEST)
