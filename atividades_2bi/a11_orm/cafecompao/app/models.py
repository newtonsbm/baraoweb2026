from django.db import models

# Create your models here.


class Feedback(models.Model):
	nome = models.CharField("Nome", max_length=100)
	email = models.EmailField("Email")
	assunto = models.CharField("Assunto", max_length=200)
	avaliacao = models.IntegerField("Avaliacao")
	telefone = models.CharField("Telefone", max_length=20, null=True, blank=True)
	mensagem = models.TextField("Mensagem")

	def __str__(self):
		return f"Feedback de {self.nome} - {self.email} - {self.assunto}"
