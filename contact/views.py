from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string

from contact.forms import ContactForm

def contato(request):
    if request.method != 'POST':
        # View da página 
        return render(request, 'contact/contact_form.html', {'form': ContactForm()})
    else:
        # Pega os dados do form
        form = ContactForm(request.POST)
        
        # Teste se é valido 
        if not form.is_valid():
            # Retorna a pág contato com os erros
            return render(request, 'contact/contact_form.html', {'form': form})

        cont = form.save()
        # Informações do email
        titulo = 'Confirmação de envio de contato'
        emailEnvia = cont.email
        emailRecebe = [cont.email , settings.DEFAULT_FROM_EMAIL]
        corpoDoEmail = render_to_string('contact/contact_email.txt', {'contact': cont})
        
        # Envia o email
        mail.send_mail(titulo, corpoDoEmail, emailEnvia, emailRecebe)

        # Retorna a pag contato com uma mensagem de sucesso de contato 
        messages.success(request, 'Contato redirecionado ao staff com sucesso!')
        return HttpResponseRedirect('/contato/')



