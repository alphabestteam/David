from rest_framework import serializers

from .models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['username', 'email', 'phone_number', 'min_work_hours', 'id']
