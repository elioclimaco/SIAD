from django.conf.urls import url, patterns

from .views import *

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name = 'Index'),
    url(r'^listar/(?P<pk>\d+)/$', DepositosListar.as_view(), name = 'Listar'),
    url(r'^formulario/(?P<action>.*)$', departmentAction, name='Accion'),

    # Exportar a CSV
    url(r'^exportarCSV/$', DepositoCSV, 'exportarCSV'),

    url(r'^prueba/$', Prueba.as_view())
)
