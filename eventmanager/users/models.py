from django.db import models
from chats.models import Message


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    user_id = models.IntegerField(primary_key=True, default=1)
    email = models.EmailField(max_length=200)
    unread_messages = models.ManyToManyField(Message, related_name="users", blank=True)

    def __str__(self):
        return f"{self.username}"
