# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {"chave teste": "Valor teste"}
    return render(request, "cotacao_grafico/pages/home.html", {'context': context, })
    # return HttpResponse("Hello")

