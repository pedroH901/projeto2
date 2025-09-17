from django import forms 

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border rounded'}))
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded', 'rows': 5}))
    