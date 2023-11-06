from django.db import models


# Create your models here.
class Chat(models.Model):
    chat_id = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.chat_id}"


class Message(models.Model):
    text = models.TextField(max_length=5000)
    chat = models.OneToOneField(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text}"
