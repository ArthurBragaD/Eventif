from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string

from contact.forms import contatoForm

def contato(request):
    if request.method != 'POST':
        # View da página 
        return render(request, 'contact/contact_form.html', {'form': contatoForm()})
    else:
        # Pega os dados do form
        form = contatoForm(request.POST)
        
        # Teste se é valido 
        if not form.is_valid():
            # Retorna a pág contatoView com os erros
            return render(request, 'contact/contact_form.html', {'form': form})

        # Informações do email
        titulo = 'Confirmação de envio de contato'
        emailEnvia = settings.DEFAULT_FROM_EMAIL
        emailRecebe = form.cleaned_data['email']
        corpoDoEmail = render_to_string('contact/contact_email.txt', form.cleaned_data)
        
        # Envia o email
        mail.send_mail(titulo, corpoDoEmail, emailEnvia, [emailEnvia, emailRecebe])

        # Retorna a pag contatoView com uma mensagem de sucesso de contato 
        messages.success(request, 'Contato redirecionado ao staff com sucesso!')
        return HttpResponseRedirect('/contatoView/')



