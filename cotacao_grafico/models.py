from django.db import models

# Create your models here.


class Precos(models.Model):
    preco = models.FloatField()
    moeda = models.CharField(max_length=30)
    data = models.DateField()

    def getDict(moeda, start_date, end_date):
        '''Gera dados para renderizar grafico
            :param moeda: str
            :param start_date: str
            :param end_date: str

            :return dicionario com lista de precos, lista de datas e moeda
        '''
        listaPrecos = []
        listaDatas = []
        dict1 = dict()
        precos = Precos.objects.filter(moeda=moeda).filter(data__range=[start_date, end_date]).order_by('data')
        for preco in precos:
            listaPrecos.append(preco.preco)
            listaDatas.append(preco.data)

        dict1['moeda'] = moeda
        dict1['precos'] = listaPrecos
        dict1['data'] = listaDatas

        return dict1


    def __str__(self):
        return str(self.data)  + ' - ' + self.moeda + ' - ' + str(self.preco)
