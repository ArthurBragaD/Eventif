from django.shortcuts import render

def contato(request):
    return render(request, 'contact/contact_form.html')