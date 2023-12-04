from datetime import datetime
from django.test import TestCase
from contact.models import Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.obj = Contact(
            name="Arthur Braga",
            email="Arthurbragadutra@gmail.com",
            phone="53912345678",
            message="teste",
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Contact.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Arthur Braga', str(self.obj))