# receitas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import Receita
from .forms import ContatoForm 

# VIEW PRINCIPAL (HOME E FILTRO DE CATEGORIA)
def home(request, categoria_nome=None):
    """
    Esta view lida com a página inicial e a filtragem por categorias.
    """
    # Busca todas as categorias distintas para exibir nos botões
    categorias = Receita.objects.values_list('categoria', flat=True).distinct()

    if categoria_nome:
        # Se uma categoria foi passada pela URL, filtra as receitas
        receitas = Receita.objects.filter(categoria__iexact=categoria_nome)
    else:
        # Se não, busca todas as receitas
        receitas = Receita.objects.all()

    context = {
        'receitas': receitas,
        'categorias': categorias,
        'active_categoria': categoria_nome,  # Para saber qual botão destacar
    }
    return render(request, 'receitas/home.html', context)


# VIEW PARA A PÁGINA DE DETALHES DA RECEITA
def receita_detail(request, id):
    """
    Exibe uma única receita em detalhe.
    """
    receita = get_object_or_404(Receita, pk=id)
    categorias = Receita.objects.values_list('categoria', flat=True).distinct()
    context = {
        'receita': receita,
        'categorias': categorias,
    }
    return render(request, 'receitas/receita_detail.html', context)


# VIEW PARA A PÁGINA DE PESQUISA
def pesquisar_receitas(request):
    """
    Lida com a página de busca dedicada.
    """
    receitas = []
    query = request.GET.get('q')
    categorias = Receita.objects.values_list('categoria', flat=True).distinct()

    if query:
        # Filtra as receitas cujo título contém o termo da busca
        receitas = Receita.objects.filter(title__icontains=query)

    context = {
        'receitas': receitas,
        'query': query,
        'categorias': categorias,
    }
    return render(request, 'receitas/pesquisar_receitas.html', context)


# VIEW PARA A PÁGINA "SOBRE NÓS"
def sobre_nos(request):
    """
    Renderiza a página 'Sobre Nós'.
    """
    categorias = Receita.objects.values_list('categoria', flat=True).distinct()
    return render(request, 'receitas/sobre_nos.html', {'categorias': categorias})


# VIEW PARA A PÁGINA DE CONTATO (ainda depende de forms.py)
def contato(request):
    """
    Lida com a exibição e o processamento do formulário de contato.
    """
    categorias = Receita.objects.values_list('categoria', flat=True).distinct()

    if request.method == 'POST':
        # Se o formulário foi enviado, preenche o form com os dados
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Se os dados são válidos, extrai as informações
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            # Lógica para enviar o email (lembre-se de configurar o email em settings.py)
            send_mail(
                subject=f'Mensagem de Contato de {nome}',
                message=f'Nome: {nome}\nEmail: {email}\n\nMensagem:\n{mensagem}',
                from_email=email, # E-mail do remetente
                recipient_list=['seu_email_de_destino@exemplo.com'], # Para quem você quer enviar
                fail_silently=False,
            )
            # Redireciona para uma página de sucesso
            return redirect('sucesso')
    else:
        # Se for a primeira vez na página (GET), cria um formulário vazio
        form = ContatoForm()

    context = {
        'form': form,
        'categorias': categorias,
    }
    return render(request, 'receitas/contato.html', context)

def sucesso(request):
    """
    Página de agradecimento após o envio do formulário.
    """
    categorias = Receita.objects.values_list('categoria', flat=True).distinct()
    return render(request, 'receitas/sucesso.html', {'categorias': categorias})