from django.shortcuts import render

def contato(request):
    return render(request, 'contato/contact_form.html')