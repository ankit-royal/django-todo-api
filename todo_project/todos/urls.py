from django.urls import path
from .views import ListTodo, TodoCreate, TodoUpdataDelete, DueTodayTasks

urlpatterns = [
    path("tasks/", ListTodo.as_view(), name="todo_list"),
    path("tasks/", TodoCreate.as_view(), name="new_todo"),
    path("tasks/<int:pk>/", TodoUpdataDelete.as_view(), name="todo_detail"),
    path('tasks/due-today/', DueTodayTasks.as_view(), name='tasks-due-today'),
]
