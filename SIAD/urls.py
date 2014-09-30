# -*- coding: utf-8 -*-
from pickle import PUT
from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from Instancias.views import DistritoViewSet, SedeViewSet, InstanciaViewSet
from WebServices.views import *

router = routers.DefaultRouter()
router.register(r'ws/Distritos', DistritoViewSet)
router.register(r'ws/Sedes', SedeViewSet)
router.register(r'ws/Instancias', InstanciaViewSet)

router.register(r'WS/Distrito/Arbol', Distrito, base_name = 'ArbolDistrito')
router.register(r'WS/Sede/Arbol', Sede, base_name = 'ArbolSede')
router.register(r'WS/Juzgado/Arbol', Juzgado, base_name = 'ArbolJuzgado')

# WS/Depositos/Juzgado/1
router.register(r'WS/Depositos/Juzgado', DepositosListar, base_name = 'DepositoListar')
#url(r'^sede/(?P<pk>\d+)/$', SedeListar.as_view(), name = 'Sede'),


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SIAD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^instancias/', include('Instancias.urls', namespace = 'Instancias')),
    url(r'^ws/', include('WebServices.urls', namespace = 'WS')),


    #
    # SERIALIZERS
    # Enlazando nuestra API usando el ruteo automático de URL's
    url(r'^', include(router.urls)),

    # Incluyendo las URL's para la API navegable
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    #url(r'insta')

    #
    # DEPÓSITOS
    #
    url(r'^depositos/', include('Depositos.urls', namespace = 'Depositos')),
)



