# -*- coding: utf-8 -*-

from django.forms import *
from django import forms
from .models import *

class DepartmentForm(ModelForm):
    class Meta:
        model = Deposito
        exclude = ['Instancia', 'Entrega', 'Secretario', 'Entregado']
        widgets = {
            'Ingreso': TextInput(attrs={'class': 'easyui-datebox',}),
        }


class DepositoNuevo(ModelForm):
    class Meta:
        model = Deposito
        exclude = ['Entrega', 'Secretario', 'Entregado']
        widgets = {
            'Ingreso': TextInput(attrs={'class': 'easyui-datebox',}),
        }


class DepositoEntregar(ModelForm):
    #Entregado   = forms.BooleanField(initial=True)
    #'my_field':True
    class Meta:
        model = Deposito
        exclude = ['Instancia', 'Numero', 'Monto', 'Ingreso', 'Expediente']
        widgets = \
        {
            'Entrega': TextInput(attrs={'class': 'easyui-datebox',}),
            #'Entregado': CheckboxInput(attrs={'checked' : 'checked', 'disabled': 'disabled', 'initial': '1'}),
            'Entregado': CheckboxInput(attrs={'checked' : 'checked',}),
        }

    # Entregado   = forms.BooleanField\
    # (
    #     label           = 'Entregado:',
    #     initial         = True,
    #     required        = True,
    #
    #     #widget          = forms.BooleanField
    #     #(
    #     #    default = True
    #     #)
    # )


    # Instancia   = models.ForeignKey(InstanciaJudicial)
    # Numero      = models.CharField(max_length = 13)
    # Monto       = models.DecimalField(max_digits=9, decimal_places=2)
    # Ingreso     = models.DateTimeField(null = True)
    # Entrega     = models.DateTimeField(null = True)
    # Expediente  = models.CharField(max_length = 50)
    # Secretario  = models.CharField(max_length = 100, null = True)
    # Entregado   = models.BooleanField(default = False)
# class AclUserForm(ModelForm):
#     class Meta:
#         model = SedeJudicial
#         exclude = ['createdate','modifydate','author']
#         widgets = {
#             'birthday': TextInput(attrs={'class': 'easyui-datebox',}),
#             'department': Select(attrs={'class': 'easyui-combogrid','data-options': '''
#             	panelWidth: 500,
#             	url: '/department/find',
#             	idField: 'id',
#             	textField: 'name',
#             	mode: 'local',
#             	fitColumns: true,
#             	columns: [[
#                     {field: 'id', title: 'Item ID', width: 60, checkbox: true},
#                     {field: 'code', title: 'Código', width: 80},
#                     {field: 'name', title: 'Nombre', align: 'right', width: 60}
#                 ]],
#             	filter: function(q, row) {
#                 	return (row.code != null && row.code.indexOf(q) >= 0 || row.name != null && row.name.indexOf(q) >= 0);
#             	}'''
#             })
#         }
