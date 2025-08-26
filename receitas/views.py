# receitas/views.py
from django.shortcuts import render, get_object_or_404
from .models import Receita

def home(request):
    # Pega o parâmetro de busca da URL (ex: /?q=bolo)
    query = request.GET.get('q')

    if query:
        # Se houver uma busca, filtra as receitas pelo título
        receitas = Receita.objects.filter(title__icontains=query)
    else:
        # Se não, mostra todas as receitas
        receitas = Receita.objects.all()

    # Envia o dicionário {'receitas': receitas} para o template
    return render(request, 'receitas/home.html', {'receitas': receitas})

def receita_detail(request, id):
    # Busca a receita pelo ID ou retorna um erro 404
    receita = get_object_or_404(Receita, pk=id)
    return render(request, 'receitas/receita_detail.html', {'receita': receita})