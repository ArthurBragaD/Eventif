from django.db import models


class Contact(models.Model):
    name = models.CharField('nome', max_length=200)
    email = models.EmailField('e-mail', blank=True)
    phone = models.CharField('telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)
    message = models.TextField("mensagem")
    response = models.TextField("resposta")

    class Meta:
        verbose_name_plural = "contatos"
        verbose_name = "contato"
        ordering = ['-created_at',]

    def __str__(self):
        return self.name
