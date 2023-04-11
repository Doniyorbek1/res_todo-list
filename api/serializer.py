from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "task": instance.task,
            "update_at": instance.update_at,
        }