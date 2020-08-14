from django.db import models

# Create your models here.
class Quiz(models.Model):
    ANSWERS_CHOICES =( 
        ("A", "A"), 
        ("B", "B"), 
        ("C", "C"), 
        ("D", "D"), 
        ("E", "E"), 
    ) 

    pergunta = models.TextField("Pergunta", max_length=500)
    alternativa1 = models.CharField("Alternativa A", max_length=200)
    alternativa2 = models.CharField("Alternativa B", max_length=200)
    alternativa3 = models.CharField("Alternativa C", max_length=200)
    alternativa4 = models.CharField("Alternativa D", max_length=200)
    alternativa5 = models.CharField("Alternativa E", max_length=200)
    resposta = models.CharField("Resposta", max_length=5, choices=ANSWERS_CHOICES)

    def __str__(self):
        return self.pergunta