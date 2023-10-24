from rest_framework import serializers
from .models import Book, Author, Message, User


class BookSerializer(serializers.ModelSerializer):
    desc_length = serializers.SerializerMethodField('get_desc_length')
    created_time = serializers.DateTimeField(read_only=True)
    author = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

    def get_desc_length(self, instance):
        return len(instance.description)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'content', 'timestamp')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 1
