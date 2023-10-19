from rest_framework import serializers
from .models import Person, Parent


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.birthDate = validated_data.get("birth_date", instance.birthDate)
        instance.homeTown = validated_data.get("city", instance.homeTown)
        instance.save()
        return instance

    def get_parents(self, instance):
        return ParentSerializer(instance.parents.all(), many=True).data


class ParentSerializer(PersonSerializer):
    class Meta:
        model = Parent
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.work = validated_data.get("work_place", instance.work_place)
        instance.baseSalary = validated_data.get("salary", instance.salary)
        super(PersonSerializer, self).update(instance, validated_data)
        return instance
