from django.shortcuts import render, redirect
from .models import *

def list_tasks(request):
    tasks = tasksdb.objects.all()
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def create_task(request):
    task = tasksdb(task=request.POST['task'], description=request.POST['description'])
    task.save()
    return redirect("/")

def delete_task(request, task_id):
    task = tasksdb.objects.get(id=task_id)
    task.delete()
    return redirect("/")

# Create your views here.
