from django.shortcuts import render

# Create your views here.

def listar_tarefa(request):
    nome_tarefa = "Olá Dara, essa é sua primeira tarefa!"
    return render(request, 'tarefas/listar_tarefas.html', {"nome_tarefa": nome_tarefa})
