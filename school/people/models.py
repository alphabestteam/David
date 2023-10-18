from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=9, primary_key=True)
    birth_date = models.DateField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Birth Date: {self.birth_date}, City: {self.city}"


class Parent(Person):
    work_place = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    children = models.ManyToManyField(Person, related_name="parents", default=[])

