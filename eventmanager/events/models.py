from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=30)
    open_date = models.DateTimeField(auto_now=True)
    close_date = models.DateTimeField(null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
    can_draft = models.BooleanField(default=False)
    can_archive = models.BooleanField(default=False)
    connected_users = models.ManyToManyField(User, related_name='connected_users')

    def __str__(self):
        return f"{self.title}"


class EventChat(Event):
    chat = models.OneToOneField(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class EventFile(Event):
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return f"{self.title}"

