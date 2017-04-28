from ..models import Report
from django.db import transaction,IntegrityError
from django.shortcuts import get_object_or_404
from personalia.script import EmpReport,perMonRep

scriptAct = {
    'empProgress' : EmpReport.ConstructReport,
    'perMonRep' : perMonRep.ConstructReport,
}

def GetEmpReport():
    report = Report.objects.all().filter(group_report='EMP',is_enable=True)
    report = {
        'report':report,
        'action_id' : '21',
    }
    return report

def GetContext(request,params):
    reports = get_object_or_404(Report,pk=params['params'])
    params['report_name'] = reports.report_name
    params['reports'] = reports
    return params

def ConstructReport(response,params):
    script_name = params['reports'].script_name
    response = scriptAct[script_name](response,params)
    return response
