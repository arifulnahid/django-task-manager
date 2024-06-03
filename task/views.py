from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
# Create your views here.


def task(request):
    tasks = Task.objects.all()
    return render(request, 'task.html', {'tasks': tasks})


def add_task(request):
    task_form = TaskForm()
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('task')
    return render(request, 'task.html', {'form': task_form})


def edit_task(request, id):
    try:
        task = Task.objects.get(pk=id)
        task_form = TaskForm(instance=task)
        if request.method == 'POST':
            task_form = TaskForm(request.POST, instance=task)
            if task_form.is_valid():
                task_form.save()
                return redirect('task')
        return render(request, 'task.html', {'form': task_form})
    except:
        return redirect('task')


def delete_task(request, id):
    try:
        task = Task.objects.get(pk=id)
        task.delete()
        return redirect('task')
    except:
        return redirect('task')
