from rest_framework import serializers

from .models import leiloeiro


class leiloeiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = leiloeiro
        fields = '__all__'

class matriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'matriculas'
        fields = '__all__'
        
class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Estado'
        fields = '__all__'

class AnexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Anexo'
        fields = '__all__'               