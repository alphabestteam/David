from rest_framework import serializers
from .models import Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = "__all__"

    def create(self, validated_data):
        return Target(**validated_data)

    def update(self, instance, validated_data):
        # Implement here an update function
        return instance
