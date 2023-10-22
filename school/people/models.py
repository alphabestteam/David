from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=9, primary_key=True)
    birthDate = models.DateField()
    homeTown = models.CharField(max_length=100)

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Birth Date: {self.birthDate}, City: {self.homeTown}"


class Parent(Person):
    work = models.CharField(max_length=100)
    baseSalary = models.IntegerField(default=0, validators=[MaxValueValidator(999999)])
    children = models.ManyToManyField(Person, related_name="parents", default=[])

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Birth Date: {self.birthDate}, City: {self.homeTown}, Work: {self.work}, Salary: {self.baseSalary}, Children: {self.children}"
