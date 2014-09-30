from django.db import models

from Instancias.models import InstanciaJudicial

class Deposito(models.Model):
    Instancia   = models.ForeignKey(InstanciaJudicial)
    Numero      = models.CharField(max_length = 13)
    Monto       = models.DecimalField(max_digits=9, decimal_places=2)
    Ingreso     = models.DateTimeField(null = True)
    Entrega     = models.DateTimeField(null = True)
    Expediente  = models.CharField(max_length = 50)
    Secretario  = models.CharField(max_length = 100, null = True)
    Entregado   = models.BooleanField(default = False)

    # def FormatoDateTime(self):
    #     resultado = self.Ingreso
    #     return resultado
    # http://stackoverflow.com/questions/19373766/django-rest-framework-custom-serialize-a-field

    def __unicode__(self):
        return self.Numero