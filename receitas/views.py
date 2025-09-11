# receitas/views.py
from django.shortcuts import render, get_object_or_404
from .models import Receita

def home(request):
    # Busca todas as receitas do banco de dados
    receitas = Receita.objects.all()
    
    # Envia a lista de receitas para o template
    context = {
        'receitas': receitas
    }
    return render(request, 'receitas/home.html', context)

def receita_detail(request, id):
    receita = get_object_or_404(Receita, pk=id)
    context = {
        'receita': receita
    }
    return render(request, 'receitas/receita_detail.html', context)

def home(request):
    receitas = Receita.objects.all()
    context = {
        'receitas': receitas
    }
    return render(request, 'receitas/home.html', context)

def receita_detail(request, id):
    receita = get_object_or_404(Receita, pk=id)
    context = {
        'receita': receita
    }
    return render(request, 'receitas/receita_detail.html', context)

# NOVA VIEW PARA A PÁGINA DE PESQUISA
def pesquisar_receitas(request):
    receitas = []
    query = request.GET.get('q') # Pega o termo de busca da URL

    if query:
        # Se um termo foi buscado, filtra as receitas
        receitas = Receita.objects.filter(title__icontains=query)

    context = {
        'receitas': receitas,
        'query': query, # Envia o termo de volta para o template
    }
    return render(request, 'receitas/pesquisar_receitas.html', context)