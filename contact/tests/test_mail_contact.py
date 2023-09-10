from django.test import TestCase
from django.core import mail

class MailTestContatoCompleto(TestCase):
    #Definindo as variaveis 
    def setUp(self):
        data = dict(name='Arthur Braga', email='Arthurbragadutra@gmail.com', phone='53 91234-5678' , message='Testando contato')
        self.response = self.client.post('/contatoView/', data)
        self.email = mail.outbox[0]

    def test_contact_email_subject(self):
        expect = 'Confirmação de envio de contato'
        self.assertEqual(expect, self.email.subject)

    def test_contact_email_sender(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_contact_email_to(self):
        expect = ['contato@eventif.com.br', 'Arthurbragadutra@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_contact_email_body(self):
        contents = ('Arthur Braga', 'Arthurbragadutra@gmail.com', '53 91234-5678', 'Testando contato')
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)


class MailTestContatoSemTelefone(TestCase):
    #Definindo as variaveis sem telefone
    def setUp(self):
        data = dict(name='Arthur Braga', email='Arthurbragadutra@gmail.com', phone='' , message='Testando contato')
        self.response = self.client.post('/contatoView/', data)
        self.email = mail.outbox[0]

    def test_contact_email_subject(self):
        expect = 'Confirmação de envio de contato'
        self.assertEqual(expect, self.email.subject)

    def test_contact_email_sender(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_contact_email_to(self):
        expect = ['contato@eventif.com.br', 'Arthurbragadutra@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_contact_email_body(self):
        contents = ('Arthur Braga', 'Arthurbragadutra@gmail.com', '', 'Testando contato')
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)