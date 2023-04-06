from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.Serializer):
    task = serializers.CharField()
    description = serializers.CharField()
    