from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path("", views.list_tasks, name="list_tasks"),
    path("new_task/", views.create_task, name="create_task"),    
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task")
]
