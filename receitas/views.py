# receitas/views.py
from django.shortcuts import render, get_object_or_404
from .models import Receita

def home(request):
    # Pega o parâmetro de busca da URL (ex: /?q=bolo)
    categoria_slug = request.GET.get('categoria')

    categoria_choices = [choice[0] for choice in Receita.CATEGORIAS]

    if categoria_slug:
        # Se houver uma busca, filtra as receitas pelo título
        receitas = Receita.objects.filter(categoria=categoria_slug)
        categoria_selecionada = categoria_slug
    else:
        # Se não, mostra todas as receitas
        receitas = Receita.objects.all()
        categoria_selecionada = None

    # Envia o dicionário {'receitas': receitas} para o template
    return render(request, 'receitas/home.html', {'receitas': receitas, 'categorias': categoria_choices, 'categoria_selecionada': categoria_selecionada})

def receita_detail(request, id):
    # Busca a receita pelo ID ou retorna um erro 404
    receita = get_object_or_404(Receita, pk=id)
    return render(request, 'receitas/receita_detail.html', {'receita': receita})