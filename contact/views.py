from django.shortcuts import render

def contato(request):
    return render(request, 'contact/template/contact_form.html')