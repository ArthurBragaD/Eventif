from django.test import TestCase


class contactGet(TestCase):
    def setUp(self):
        self.response = self.client.get('/contatoView/')
# 
    def test_get(self):
        """GET /contatoView/ must return status_code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use contact/contact_form.html"""
        self.assertTemplateUsed(self.response, 'contact/contact_form.html')

    # def test_html(self):
    #     """HTML must contain input tags"""
    #     tags = (
    #         ('<form', 1), 
    #         ('<input', 6), 
    #         ('type="text"', 3), 
    #         ('type="email"', 1), 
    #         ('type="submit"', 1)
    #     )
    #     for text, count in tags:
    #         with self.subTest():
    #             self.assertContains(self.response, text, count)
