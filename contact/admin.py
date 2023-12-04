from django.contrib import admin
from django.conf import settings
from django.utils.timezone import now
from contact.models import Contact
from django.core import mail
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at', 'updated_at', 'message', 'response']
    date_hierarchy = 'created_at'
    search_fields = ['name', 'email', 'phone', 'created_at', 'updated_at', 'message', 'response']
    list_filter = ['created_at', 'updated_at']

    actions = ["responder"]

    def responder(self, request, queryset):
        for contact in queryset:
            resposta = queryset.update(response="Mensagem foi marcada como respondida")
            nome = contact.name
            emailEnvia = settings.DEFAULT_FROM_EMAIL
            # if (contact.phone == ""):
            #     telefone = "Não informado"
            # else:
            telefone = contact.phone
            emailRecebe = [contact.email , settings.DEFAULT_FROM_EMAIL]
            corpoDoEmail = render_to_string('contact/contact_response.txt', {'contact': contact})
            mail.send_mail(
                nome,
                corpoDoEmail,
                emailEnvia,
                emailRecebe,
                telefone,
                resposta
            )
        self.message_user(request, f'{queryset.count()} contato(s) foi(ram) respondido(s) com sucesso.')
        return HttpResponseRedirect('/admin/contact/contact/')
    responder.short_description = 'Enviar resposta para contatos selecionados'


admin.site.register(Contact, ContactModelAdmin)