from django.test import TestCase
from django.test import SubscriptionForm

class subscriptionFromTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        self.assertSequenceEqual(['name','cpf','email','phone'], list(self.form.fields))