# from django.http import HttpResponse
from django.shortcuts import render

from cotacao_grafico.models import Precos


def home(request):
    # todo     ################   hard coded 

    print(request)
    moeda = request.GET.get('moeda')
    inicio = request.GET.get('inicio')
    fim = request.GET.get('fim')

    print("\n#########")
    print(moeda)
    print(inicio)
    print(fim)

    context = Precos.getDicionarioParaGrafico(moeda, inicio, fim)
    print(context)
    return render(request, "cotacao_grafico/pages/home.html", {'context': context, })
