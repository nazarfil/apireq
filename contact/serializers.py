from rest_framework import serializers

from contact.models import Contact
from contact.models import ResearchRequest
from contact.models import UserData

class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField()
    message = serializers.CharField();

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Contact.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.email)
        instance.message = validated_data.get('message', instance.message)
        instance.save()
        return instance

class UserDataSerializer(serializers.Serializer):
    hash = serializers.CharField()
    age = serializers.IntegerField()
    illnesss = serializers.CharField()

    def create(self, validated_data):
        return UserData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.hash = validated_data.get('hash', instance.hash)
        age = validated_data.get('age', instance.age)
        illnesss = validated_data.get('ilness', instance.illnesss)
        return instance

class ResearchRequestSerializer(serializers.Serializer):
    address = serializers.CharField()
    name = serializers.CharField()
    category = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return ResearchRequest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.address = validated_data.get('address', instance.address)
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.start_date = validated_data.get('start_date', instance.end_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        return instance