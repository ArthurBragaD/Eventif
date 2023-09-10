from django.test import TestCase
from contact.forms import contatoForm

class contatoFormTest(TestCase):
    def setUp(self):
        self.form = contatoForm()

    def test_form_has_fields(self):
        self.assertSequenceEqual(['name', 'email', 'phone', 'message'], list(self.form.fields))