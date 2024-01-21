from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Worker(AbstractUser):
    min_work_hours = models.PositiveIntegerField(null=False, blank=False)
    phone_number = models.CharField(max_length=10)
    groups = None
    user_permissions = None
