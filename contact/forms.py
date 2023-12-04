from django import forms

class contatoForm(forms.Form):
    #Criação do form
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    #Telefone sem valor gera Não informado
    phone = forms.CharField(label='Telefone', empty_value='Não informado')
    #Atributo do message vira Textarea
    message = forms.CharField(label='Mensagem',widget=forms.Textarea)