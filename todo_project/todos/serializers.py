from rest_framework import serializers
from .models import Todo
from datetime import date


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_due_date(self, value):
        if value and value <= date.today():
            raise serializers.ValidationError("Due date must be a future date.")
        return value