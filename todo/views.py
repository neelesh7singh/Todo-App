from django.shortcuts import render, redirect
from django.utils import timezone
from . import models


# Create your views here.

def home(request):
    todo_list = models.Todo.objects.all().order_by('-added_date')
    stuff_for_frontend = {
        'todos': todo_list
    }
    return render(request, 'base.html', stuff_for_frontend)


def add_todo(request):
    if request.POST.get('todo').strip() != '':
        curr_time = timezone.now()
        obj = models.Todo.objects.create(added_date=curr_time, text=request.POST.get('todo'))
        obj.save()
    return redirect('home')


def delete_todo(request, todo_id):
    obj = models.Todo.objects.get(id=todo_id)
    obj.delete()
    return redirect('home')
