from cotacao_grafico.models import Precos
from rest_framework import serializers


class PrecosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Precos
        fields = (
            'moeda',
            'data',
            'preco',
        )
