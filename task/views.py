from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    tasks = task.objects.all
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'task/index.html', {'task' : tasks, 'form' : form})

def updateTask(request, pk):
    tasks = task.objects.get(id = pk)
    form = TaskForm(instance = tasks)
    if request.method == 'POST':
            form = TaskForm(request.POST, instance = tasks)
            if form.is_valid():
                form.save()
            return redirect('/')
    return render(request, 'task/update.html', {'task' : tasks, 'form' : form})

def delTask(request, pk):
    item = task.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'task/delete.html', {'item' : item})





