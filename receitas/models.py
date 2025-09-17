# receitas/models.py
from django.db import models

class Receita(models.Model):
    # Adicionamos as opções de categoria aqui
    CATEGORIAS = [
        ('BOLOS', 'Bolos'),
        ('TORTAS', 'Tortas'),
        ('CARNES', 'Carnes'),
        ('SALADAS', 'Saladas'),
        ('SOPAS', 'Sopas'),
        ('BEBIDAS', 'Bebidas'),
        ('OUTROS', 'Outros'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    # Adicionamos o novo campo 'categoria'
    categoria = models.CharField(max_length=100, choices=CATEGORIAS)
    image = models.ImageField(upload_to='receitas/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title