from django.test import TestCase
from contact.admin import ContactModelAdmin, Contact, admin

from unittest.mock import Mock


class ContactModelAdminTest(TestCase):
    def setUp(self):
        Contact.objects.create(
            name="Arthur Braga",
            email="Arthurbragadutra@gmail.com",
            phone="53912345678",
            message="Teste"
        )

        self.model_admin = ContactModelAdmin(Contact, admin.site)

    def call_action(self):
        queryset = Contact.objects.all()

        self.mock = Mock()
        old_message_user = ContactModelAdmin.message_user

        ContactModelAdmin.message_user = self.mock

        ContactModelAdmin.message_user = old_message_user

