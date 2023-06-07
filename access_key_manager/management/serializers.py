from rest_framework import serializers
from .models import Key

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Key
        fields = '__all__'

    def create(self, validate_data):
        instance = Key.objects.create(**validate_data)# `**validate_data` unpacks all the instances of the field
        return instance


