from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer
from django.shortcuts import get_object_or_404
from django.utils.timezone import now

# Create your views here.


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoUpdataDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DueTodayTasks(APIView):
    def get(self, request, *args, **kwargs):
        today = now().date()
        tasks_due_today = Todo.objects.filter(due_date=today)
        serializer = TodoSerializer(tasks_due_today, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
