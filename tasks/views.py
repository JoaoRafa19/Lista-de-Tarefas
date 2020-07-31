from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarefa
from .forms import TarefaForm

# Create your views here.
def index(request):
    data = {}
    data['tarefas'] = Tarefa.objects.all()
    return render(request, 'tasks/index.html', data)


def adicionar_tarefa(request):
    data = { }
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    data['form'] = form
    return render(request, 'tasks/form.html', data)


def update_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    form = TarefaForm(request.POST or None, instance=tarefa)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'tasks/form.html', {'form':form, 'tarefa':tarefa})


def delete_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()
    return redirect('index')