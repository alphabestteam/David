from rest_framework import serializers
from .models import Person, Parent


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

    def get_parents(self, instance):
        return ParentSerializer(instance.parents.all(), many=True).data


class ParentSerializer(PersonSerializer):
    class Meta:
        model = Parent
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.work_place = validated_data.get("work_place", instance.work_place)
        instance.salary = validated_data.get("salary", instance.salary)
        super(PersonSerializer, self).update(instance, validated_data)
        return instance
