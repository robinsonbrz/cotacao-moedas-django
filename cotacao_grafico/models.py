import json
from datetime import date, datetime, timedelta

import holidays
import requests
from bdateutil import isbday
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
        QTD_DIAS_RENDERIZA = 5
        listaPrecos = []
        listaDatas = []
        dict1 = dict()
        dict1['erro'] = ''

        # valida campos em branco
        if moeda is None:
            dict1['erro'] = 'Campo moeda vazio<br>'
            moeda = "BRL"
        if start_date is None:
            dict1['erro'] += 'Campo inicio vazio<br>'
            start_date = "2022-06-29"
        if end_date is None or end_date == "":
            dict1['erro'] += 'Campo data vazio foi substituido<br>'
            end_date = date.today().strftime("%Y-%m-%d")
            start_date = (date.today() - timedelta(days=5)).strftime("%Y-%m-%d")


        # valida se data inicial é maior que final
        inicio = datetime.strptime(start_date, "%Y-%m-%d")
        fim = datetime.strptime(end_date, "%Y-%m-%d")

        if (inicio > fim) or (fim > datetime.today() ):
            dict1['inicio'] = start_date
            dict1['fim'] = end_date
            dict1['erro'] = 'Data inicial mais recente que data final <br>Ou futura data inválida ' 
            return dict1

        count = 0
        temp_date = inicio
        # valida quantidade de dias 
        while temp_date <= fim:
            #preco = Precos.objects.filter(data=inicio)
            existeEmBD = Precos.objects.filter(moeda=moeda).filter(data=temp_date).order_by('data').exists()
            precos = Precos.objects.filter(moeda=moeda).filter(data=temp_date).order_by('data')
            if not existeEmBD:
                dataPesquisa = temp_date.strftime("%Y-%m-%d")
                # Apenas chama API para dias úteis
                if isbday(temp_date, holidays=holidays.BR()) :
                    objeto_cotacoes = requests.get(f'https://api.vatcomply.com/rates?date={dataPesquisa}&base=USD').json()
                    
                    valorBRL = objeto_cotacoes['rates']['BRL']
                    valorEUR = objeto_cotacoes['rates']['EUR']
                    valorJPY = objeto_cotacoes['rates']['JPY']
                    Precos.objects.create(preco=valorBRL, moeda='BRL', data=dataPesquisa)
                    Precos.objects.create(preco=valorEUR, moeda='EUR', data=dataPesquisa)
                    Precos.objects.create(preco=valorJPY, moeda='JPY', data=dataPesquisa)
                    count += 1 
            else:
                count +=1 

            temp_date = temp_date + timedelta(days=1)
            # restrição de 5 dias úteis atingidas encerra chamadas da API
            if count > (QTD_DIAS_RENDERIZA-1):
                break

        # renderiza do banco de dados
        precos = Precos.objects.filter(moeda=moeda).filter(data__range=[start_date, end_date]).order_by('data')
        for preco in precos:
            listaPrecos.append(round(preco.preco,4))
            listaDatas.append(preco.data.strftime("%d-%m-%Y"))
        dict1['moeda'] = moeda

        dict1['precos'] = listaPrecos[0:QTD_DIAS_RENDERIZA]
        dict1['datas'] = listaDatas[0:QTD_DIAS_RENDERIZA]
        dict1['inicio'] = start_date
        dict1['fim'] = end_date
        if len(listaPrecos) > (QTD_DIAS_RENDERIZA ):
            dict1['erro'] = f'Gráfico renderiza apenas 5 dias úteis<br>{len(listaPrecos)} dias úteis solicitados'
        return dict1


    #def __str__(self):
    #    return str(self.data)  + ' - ' + self.moeda + ' - ' + str(round(self.preco,2))
