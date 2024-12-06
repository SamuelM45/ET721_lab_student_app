from django.shortcuts import render
from .models import ToDo

def todo_list(request):
    todos = ToDo.objects.all()
    return render(request, 'to_do_list/todo_list.html', {'todos': todos})
