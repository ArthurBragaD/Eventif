from django.test import TestCase
from contact.forms import ContactForm

class contatoFormTest(TestCase):
    def setUp(self):
        self.form = ContactForm()

    def testFormInformacoes(self):
        self.assertSequenceEqual(['name', 'email', 'phone', 'message'], list(self.form.fields))