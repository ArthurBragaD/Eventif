from django.contrib import admin
from django.utils.timezone import now
from contact.models import Contact


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone',
                    'created_at', 'updated_at', 'message', 'response']
    date_hierarchy = 'created_at'
    search_fields = ['name', 'email', 'phone', 'created_at', 'updated_at', 'message', 'response']
    list_filter = ['created_at', 'updated_at']

    # def contacted_today(self, obj):
    #     return obj.created_at.date() == now().date()

    # contacted_today.short_description = 'contatado hoje?'
    # contacted_today.boolean = True

admin.site.register(Contact, ContactModelAdmin)
