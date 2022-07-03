from django.db import models

# Create your models here.


class Precos(models.Model):
    preco = models.FloatField()
    moeda = models.CharField(max_length=30)
    data = models.DateField()

    def __str__(self):
        return str(self.data)  + ' - ' + self.moeda + ' - ' + str(self.preco)
