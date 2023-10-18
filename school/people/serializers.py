from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.city = validated_data.get("city", instance.city)
        instance.save()
        return instance
