from django.shortcuts import render
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from contact.forms import contatoForm

def contato(request):
    return render(request, 'contact/contact_form.html', {'form': contatoForm()})
