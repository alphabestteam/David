from django.http import HttpResponse, JsonResponse
from .models import Person
from .serializers import PeopleSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status


# Create your views here.
def get_all_people(request):
    people = Person.objects.all()
    serializer = PeopleSerializer(people, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


def add_person(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serialized = PeopleSerializer(data=data)
        if serialized.is_valid():
            serialized.create(data)
            return HttpResponse("Person was successfully added to the DB", status=status.HTTP_201_CREATED)
        return HttpResponse("Person didnt meet the requirements", status=status.HTTP_400_BAD_REQUEST)


def delete_person(request):
    pass


def update_person(request):
    if request.method == "PUT":
        data = JSONParser().parse(request)
        person_id = data["id"]
        person = Person.objects.get(id=person_id)
        serialized = PeopleSerializer(person, data=data)
        if serialized.is_valid():
            serialized.update(person, data)
            return HttpResponse("Successfully updated the person", status=status.HTTP_200_OK)
        return HttpResponse("Error: Updated details for person dont meet the requirements", status=status.HTTP_400_BAD_REQUEST)
