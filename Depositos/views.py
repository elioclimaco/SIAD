# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, CreateView, DetailView
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils import simplejson
import json

from rest_framework import viewsets
from WebServices.views import *

from .models import *
from .funciones import *
from .forms import *

from io import BytesIO
from import_export import resources



class DepositosCSV(resources.ModelResource):
    class Meta:
        model = Deposito



# Importar a CSV
import csv
from django.template import loader, Context

def DepositoCSV(request):
    """
    Convierte a CSV usando la libreria de django
    """

    # Crea un objeto HttpResponse con las cabeceras
    # CSV apropiadas.
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    # The data is hard-coded here, but you could load it from a database or
    # some other source.
    csv_data = (
        ('First row', 'Foo', 'Bar', 'Baz'),
        ('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"),
    )

    t = loader.get_template('pruebaCSV.txt')
    c = Context({
        'data': csv_data,
    })
    response.write(t.render(c))
    return response

class Prueba(TemplateView):
    template_name = 'depositos/datos.json'




class Index(TemplateView):
    """
    Muestra la página contenedora del control
    layout.
    """
    template_name = 'depositos/index.html'


class DepositosListar(DetailView):
    """
    Muestra la página contenedora del control
    datagrid.
    """
    model = InstanciaJudicial
    template_name = 'depositos/listar.html'


def departmentAction(request,action):
    if action=='query': return render_to_response('depositos/formulario.html')
    if action=='find':
        data=query(Deposito,request,{'name':'departmentName'})
        #data=query(DepositosPorJuzgado(request,1),request,{'name':'departmentName'})
        return HttpResponse(simplejson.dumps(data))
    if action=='add':
        form = DepositoNuevo(request.POST or None)
        url = '/department/add'
        if request.method == "POST":
            if form.is_valid():
                o=form.save()
                data={'success':True,'msg':"Instancia registrada correctamente",'obj':json(o),'isAdd':True}
                return HttpResponse(simplejson.dumps(data))
        t = get_template('depositos/formulario.html')
        c = RequestContext(request,locals())
        return HttpResponse(t.render(c))
    if action=='del':
        ids=request.GET['ids']
        for pk in ids.split(","):
            Deposito.objects.get(pk=pk).delete()
        data={'success':True,'msg':"Instancia eliminada correctamente",'obj':None}
        return HttpResponse(simplejson.dumps(data))
    if action.startswith('edit')>0:
        pk=action.split("/")[-1]
        instance = Deposito.objects.get(pk=pk)
        form = DepartmentForm(request.POST or None, instance = instance)
        url = '/formulario/edit/'+pk
        if request.method == "POST":
            if form.is_valid():
                o=form.save()
                data={'success':True,'msg':"Instancia modificada correctamente",'obj':json(o),'isAdd':False}
                return HttpResponse(simplejson.dumps(data))
        t = get_template('depositos/formulario.html')
        c = RequestContext(request,locals())
        return HttpResponse(t.render(c))

    if action.startswith('entregar')>0:
        pk = action.split("/")[-1]
        instance = Deposito.objects.get(pk=pk)
        form = DepositoEntregar(request.POST or None, instance=instance)
        url = '/formulario/entregar/' + pk

        if request.method == 'POST':

            if form.is_valid():
                deposito = form.save()
                data = {'success': True, 'msg': 'Depósito entregado correctamente', 'obj': json(deposito), 'isAdd': False}
                return HttpResponse(simplejson.dumps(data))

        plantilla = get_template('depositos/formulario.html')
        contexto = RequestContext(request, locals())
        return HttpResponse(plantilla.render(contexto))
