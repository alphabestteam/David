from django.urls import re_path, path
from . import views

urlpatterns = [
    path("getRandomNumber/", views.get_random_number, name="rand_num"),
    path("getRandomNumber/<number>", views.get_random_number_user_input, name="user_input_rand_num"),
    path("getServerTime/", views.get_curr_time, name="curr_time"),
    path("numOfLetters/<word>", views.get_num_of_letters, name="num_of_letters"),
]
