from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import *


class InstanciaSerializer(serializers.ModelSerializer):
    text = serializers.Field(source = 'Nombre')
    class Meta:
        model = InstanciaJudicial
        fields = ('id', 'text')


class SedeSerializer(serializers.ModelSerializer):
    text = serializers.Field(source = 'Nombre')
    # Crea un campo state para mostrar las ramas
    # cerradas.
    # state = serializers.SerializerMethodField('Estado')

    url = serializers.SerializerMethodField('Direccion')


    children = InstanciaSerializer(many = True, source = 'Instancia')
    class Meta:
        model = SedeJudicial
        # Llama a las instancias
        # fields = ('id', 'text', 'children', 'state')
        fields = ('id', 'text', 'url')

    # Define el valor del vampo state
    # def Estado(self, obj):
    #     estado = 'closed'
    #     return estado

    def Direccion(self, obj):
        a = 'sede/'
        return a

class DistSerializer(serializers.ModelSerializer):
    text = serializers.Field(source = 'Nombre')
    children = SedeSerializer(many = True, source = 'Sede')
    class Meta:
        model = DistritoJudicial
        fields = ('id', 'text', 'children')
