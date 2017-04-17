# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from .models import Menu,Action
from personalia.views_script import index,employees,leader,report,\
    coaching
from django.http import HttpResponse
from datetime import datetime

query = {
    'GetIndex':index.GetIndex,
    'GetEmloyees':employees.GetEmloyees,
    'newEmp':employees,
    'editEmp':employees,
    'GetLeader':leader.GetLeader,
    'GetReport':report.GetEmpReport,
    'GetEmpReport':report,
    'GetCoaching':coaching.GetCoaching,
    'newCoach':coaching,
    'GetCoarchReport':coaching,
}

def index(request):
    return render(request,'personalia/index.html')

def menuShow(request,menu_id):
    menu = Menu.objects.get(pk=menu_id)
    action = Action.objects.all().filter(menu_id=menu.menu_id,is_enable=True)
    variable = query[menu.query_function]()
    return render(request,menu.templatesource,{
        'variable' : variable,'menu' : menu,'action' : action,
    })

def actionShow(request,action_id,params):
    action = Action.objects.get(pk=action_id)
    params = {'action':action,'params':params}
    #raise Exception,action.query_function
    context = query[action.query_function].GetContext(request,params)
    if action.is_direct :
        date_now = datetime.today().strftime("%d%m%y %H:%M:%S")
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="%s %s.xlsx"' % (
            context['report_name'],date_now,)
        response = query[action.query_function].ConstructReport(response,context)
        return response
    else :
        return render(request,action.templatesource,context)
