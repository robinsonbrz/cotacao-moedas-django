# from django.http import HttpResponse
from django.shortcuts import render

from cotacao_grafico.models import Precos


def home(request):
    # todo     ################   hard coded 
    context = Precos.getDict('BRL', '2022-06-29', '2022-07-03' )
    return render(request, "cotacao_grafico/pages/home.html", {'context': context, })
