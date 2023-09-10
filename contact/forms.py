from django import forms

class contatoForm(forms.Form):
    #Criação do form
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone', empty_value='Não informado')
    message = forms.CharField(label='Mensagem',widget=forms.Textarea)