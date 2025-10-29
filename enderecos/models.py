from django.db import models

# Create your models here.

class Endereco(models.Model):
        cep - models.CharField(max_length=10)
        logradouro = models.CharField(max_length=100)
        complemento = models.CharField(max_length=100, blank=True, null=True)
        unidade = models.CharField(max_length=100)
        bairro = models.CharField(max_length=100)
        localidade = models.CharField(max_length=100)
        uf = models.CharField(max_length=2)
        regiao = models.CharField(max_length=100)
        ibge = models.CharField(max_length=10)
        gia = models.CharField(max_length=10)
        ddd = models.CharField(max_length=5)
        siafi = models.CharField(max_length=10)

        def __str__(self):
            return f"{self.logradouro}, {self.bairro}, {self.localidade} - {self.uf}, {self.cep}"
        class Meta:
              ordering = ['localidade', 'bairro', 'logradouro']
              verbose_name = "Endereço"