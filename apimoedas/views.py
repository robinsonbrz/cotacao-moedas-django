from cotacao_grafico.models import Precos
from rest_framework.response import Response
from rest_framework.views import APIView

from apimoedas.serializers import PrecosSerializer


class PrecosAPIView(APIView):
    """
    API de Consulta de moedas - Robinson Enedino
    """
    def get(self, request):

        moeda = request.GET.get('moeda')
        inicio = request.GET.get('inicio')


        # ?inicio=2022-06-29&moeda=BRL

        existeEmBD = Precos.objects.filter(moeda=moeda).filter(data=inicio).exists()
        if existeEmBD:
            preco = Precos.objects.filter(moeda=moeda).filter(data=inicio).first()
        else:
            return Response({"Erro":"Objeto não existe no Banco de Dados ou parâmetros incorretos",
                            "Exemplo":"api/v1/precos/?inicio=2022-07-04&moeda=BRL"
            })

        # preco = Precos.objects.all() 
        serializer  = PrecosSerializer(preco)
        print(serializer.data)
        return Response(serializer.data)
