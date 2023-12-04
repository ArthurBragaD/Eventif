from django.test import TestCase
from contact.forms import ContactForm

class contactGet(TestCase):
    def setUp(self):
        self.response = self.client.get('/contato/')
# 
    def test_get(self):
        #Teste para ver se o link esta ok
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        #Teste para ver se o templete usado esta correto
        self.assertTemplateUsed(self.response, 'contact/contact_form.html')

    def test_html(self):
        #Teste para ver se os testes do form do HTML estão corretos 
        tags = (
            ('<form', 1), 
            ('<input', 5), 
            ('type="text"', 2), 
            ('type="email"', 1), 
            ('<textarea', 1),
            ('type="submit"', 1)
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)