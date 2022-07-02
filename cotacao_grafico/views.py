from django.shortcuts import render

# Create your views here.


def home(request):
    context = {"chave teste": "Valor teste"}
    return render(request, "cotacao_grafico/pages/home.html", {'context': context, })
