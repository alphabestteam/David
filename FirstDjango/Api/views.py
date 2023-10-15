import random
import time
import re

from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, Django!")


def get_random_number(request):
    return HttpResponse(random.random(), status=200)


def get_random_number_user_input(request, number):
    if not number.isnumeric():
        return HttpResponse(f"<h1>Please enter only numeric values.<br>You entered {number}</h1>")
    number = float(number)
    return HttpResponse(random.uniform(0, number), status=200)


def get_curr_time(request):
    curr_time = time.localtime()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", curr_time)
    return HttpResponse(formatted_time, status=200)


def get_num_of_letters(request, word):
    if not word.isalpha():
        return HttpResponse(f"<h1>Please enter only Alphabetical values only.<br>You entered {word}</h1>")
    return HttpResponse(len(word), status=200)

