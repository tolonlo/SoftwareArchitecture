from rest_framework import serializers
from todo.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'memo', 'created', 'completed']

class ToDoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id']
        read_only_fields = ['id']