import random
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, Django!")


def get_random_number(request):
    return HttpResponse(random.random())


def get_random_number_user_input(request, number):
    return HttpResponse(random.uniform(0, number))
