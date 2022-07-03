from django.db import models

# Create your models here.


class Precos(models.Model):
    preco = models.FloatField()
    moeda = models.CharField(max_length=30)
    data = models.DateField()

    def getDicionarioParaGrafico(moeda, start_date, end_date):
        '''Gera dicionario para renderizar grafico
            :param moeda: str
            :param start_date: str
            :param end_date: str

            :return dicionario com lista de precos, lista de datas e moeda
        '''
        listaPrecos = []
        listaDatas = []
        dict1 = dict()
        
        if moeda is None:
            dict1['erro'] = 'Campo moeda vazio<br>'
            moeda = "BRL"
        if start_date is None:
            dict1['erro'] += 'Campo inicio vazio<br>'
            start_date = "2022-06-29"
        if end_date is None:
            dict1['erro'] += 'Campo data vazio<br>'
            end_date = "2022-07-03"



        precos = Precos.objects.filter(moeda=moeda).filter(data__range=[start_date, end_date]).order_by('data')
        for preco in precos:
            listaPrecos.append(round(preco.preco,2))
            listaDatas.append(preco.data.strftime("%d-%m-%Y"))
        dict1['moeda'] = moeda
        dict1['precos'] = listaPrecos
        dict1['datas'] = listaDatas
        dict1['inicio'] = start_date
        dict1['fim'] = end_date


        




        return dict1

    def __str__(self):
        return str(self.data)  + ' - ' + self.moeda + ' - ' + str(round(self.preco,2))
