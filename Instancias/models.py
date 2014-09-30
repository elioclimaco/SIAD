# -*- coding: utf-8 -*-

from django.db import models

# class DistritoJudicial(models.Model):
#     Nombre  = models.CharField(max_length = 50)
#
#     class Meta:
#         verbose_name = u'Distrito Judicial'
#         verbose_name_plural = u'Distritos Judiciales'
#
#     def __unicode__(self):
#         return self.Nombre

class DistritoJudicial(models.Model):
    Nombre = models.CharField(max_length = 50)



class SedeJudicial(models.Model):
    Distrito  = models.ForeignKey(DistritoJudicial, related_name = 'Sede')
    #Distrito  = models.ForeignKey(DistritoJudicial, related_name = 'Distrito')
    Nombre  = models.CharField(max_length = 200)

    class Meta:
        verbose_name = u'Sede Judicial'
        verbose_name_plural = u'Sedes Judiciales'

    def __unicode__(self):
        return self.Nombre


class InstanciaJudicial(models.Model):
    Sede  = models.ForeignKey(SedeJudicial, related_name = 'Instancia')
    #Sede  = models.ForeignKey(SedeJudicial, related_name = 'Sede')
    Nombre  = models.CharField(max_length = 200)

    class Meta:
        verbose_name = u'Instancia'
        verbose_name_plural = u'Órganos Jurisdiccionales'

    def __unicode__(self):
        return self.Nombre
        #return u'%s (%s)' %(self.Nombre, u','.join([sede.Nombre for sede in self.Sede.all()]))