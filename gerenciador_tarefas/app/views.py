from django.shortcuts import render
from .forms import TarefaForm

# Create your views here.

def listar_tarefa(request):
    nome_tarefa = "Olá Dara, essa é sua primeira tarefa!"
    return render(request, 'tarefas/listar_tarefas.html', {"nome_tarefa": nome_tarefa})

def cadastrar_tarefa(request):
    form_tarefa = TarefaForm()
    return render(request, 'tarefas/form_tarefa.html', {"form_tarefa": form_tarefa})