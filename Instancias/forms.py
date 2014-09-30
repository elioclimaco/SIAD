# -*- coding: utf-8 -*-

from django.forms import *

from .models import *


class agregarInstancia(ModelForm):
    class Meta:
        model = InstanciaJudicial


class DepartmentForm(ModelForm):
    class Meta:
        model = InstanciaJudicial
        exclude = ['createdate','modifydate','author']

class AclUserForm(ModelForm):
    class Meta:
        model = SedeJudicial
        exclude = ['createdate','modifydate','author']
        widgets = {
            'birthday': TextInput(attrs={'class': 'easyui-datebox',}),
            'department': Select(attrs={'class': 'easyui-combogrid','data-options': '''
            	panelWidth: 500,
            	url: '/department/find',
            	idField: 'id',
            	textField: 'name',
            	mode: 'local',
            	fitColumns: true,
            	columns: [[
                    {field: 'id', title: 'Item ID', width: 60, checkbox: true},
                    {field: 'code', title: 'Código', width: 80},
                    {field: 'name', title: 'Nombre', align: 'right', width: 60}
                ]],
            	filter: function(q, row) {
                	return (row.code != null && row.code.indexOf(q) >= 0 || row.name != null && row.name.indexOf(q) >= 0);
            	}'''
            })
        }
