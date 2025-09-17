# receitas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Rota para a página inicial (sem filtro)
    path('', views.home, name='home'),
    # NOVA ROTA: Para filtrar por categoria
    path('categoria/<str:categoria_nome>/', views.home, name='receitas_por_categoria'),
    path('receita/<int:id>/', views.receita_detail, name='receita_detail'),
    path('pesquisar/', views.pesquisar_receitas, name='pesquisar_receitas'),
    path('contato/', views.contato, name='contato'),
    path('sobre_nos/', views.sobre_nos, name='sobre_nos'),
    path('suceso/', views.sucesso, name='sucesso'),
]