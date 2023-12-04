from django.test import TestCase
from django.core import mail

class TestPostContato(TestCase):
    #Teste para ver envio do Post para envio email
    def setUp(self):
        data = dict(name='TestPostContato', email='TestPostContato@gmail.com', message='TestPostContato')
        self.response = self.client.post('/contato/', data)
        self.assertEqual(len(mail.outbox), 1)

class TestPostError(TestCase):
    #Teste para ver se post invalido gera um email
    def test_details(self):
        data = dict(name='', email='', message='')
        self.response = self.client.post("/contato/", data)
        self.assertEqual(len(mail.outbox), 0)

class TestDoTemplateDoEmail(TestCase):
    #Teste dos templates do email
    def setUp(self):
        data = dict(name='TestDoTemplate', email='TestDoTemplate@gmail.com', message='TestDoTemplate')
        self.response = self.client.post('/contato/', data)
        self.email = mail.outbox[0]
    #Titulo
    def testContatoTitulo(self):
        expect = 'Confirmação de envio de contato'
        self.assertEqual(expect, self.email.subject)
    #Quem envia
    def testContatoQuemEnvia(self):
        expect = 'TestDoTemplate@gmail.com'
        self.assertEqual(expect, self.email.from_email)
    #Para Quem
    def testContatoQuemRecebe(self):
        expect = ['TestDoTemplate@gmail.com', 'contato@eventif.com.br']
        self.assertEqual(expect, self.email.to)

class MailTestContatoCompleto(TestCase):
    #Definindo as variaveis 
    def setUp(self):
        data = dict(name='Arthur Braga', email='Arthurbragadutra@gmail.com', phone='53 91234-5678' , message='Testando contato')
        self.response = self.client.post('/contato/', data)
        self.email = mail.outbox[0]

    def testContatoInformacoes(self):
        contents = ('Arthur Braga', 'Arthurbragadutra@gmail.com', '53 91234-5678', 'Testando contato')
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)


class MailTestContatoSemTelefone(TestCase):
    #Definindo as variaveis sem telefone
    def setUp(self):
        data = dict(name='Arthur Braga', email='Arthurbragadutra@gmail.com', message='Testando contato')
        self.response = self.client.post('/contato/', data)
        self.email = mail.outbox[0]

    def testContatoInformacoes(self):
        contents = ('Arthur Braga', 'Arthurbragadutra@gmail.com', 'Testando contato')
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)