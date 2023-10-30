from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    # unread_msgs = models.ManyToManyField(Message)

    def __str__(self):
        return f"{self.username}"
