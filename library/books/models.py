from django.db import models
from rest_framework.exceptions import ValidationError


def validate_title(title):
    if len(title) < 3:
        raise ValidationError("Title is too short")


def validate_author(author):
    if len(author) < 3 or author.isdigit():
        raise ValidationError("Author name is too short")


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50, null=False, validators=[validate_author])
    age = models.PositiveIntegerField()
    author_id = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Author ID: {self.author_id}"


class Book(models.Model):
    title = models.CharField(max_length=255, validators=[validate_title])
    description = models.TextField()
    book_id = models.PositiveIntegerField(primary_key=True, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, )

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Description: {self.description}, Book ID: {self.book_id}"


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
