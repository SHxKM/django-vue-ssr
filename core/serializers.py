from rest_framework import serializers
from .models import ToDoItem

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ('id', 'title', 'created_at', 'description', 'is_done')

