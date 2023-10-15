from django.urls import path
from . import views


urlpatterns = [
    path("api/getrandomnumber/", views.get_random_number, name="randomNum"),
    path("api/getrandomnumber/<int:number>", views.get_random_number_user_input, name="randomNum"),

]

