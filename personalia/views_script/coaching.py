from personalia.models import Coaching,Employee,Report
from personalia.forms import fCoaching
from django.db import transaction,IntegrityError
from django.shortcuts import get_object_or_404
from personalia.script import CoachReport

def GetCoaching():
    employee = Employee.objects.all()
    employee = {'employee':employee,
        'action_id' : '41',
    }
    return employee

def newCoach(request,params):
    p = params
    employee = get_object_or_404(Employee,pk=p['params'])
    coachHist = Coaching.objects.filter(employee=p['params'])
    msg = {}
    form = (fCoaching(),)
    if request.method == 'POST':
        cekform = fCoaching(request.POST)
        if cekform.is_valid():
            try:
                with transaction.atomic():
                    coaching = cekform.save(commit=False)
                    coaching.employee = employee
                    coaching.save()
                    msg = 'Berhasil menyimpan data pelatihan karyawan (%s)' % (employee.person.name)
            except IntegrityError:
                form = (cekform,)
                msg = 'Gagal menyimpan'
    context = {
        'msg':msg,'form':form,'button':('Save',),'action':p['action'],
        'emp':employee,'coachHist':coachHist,'action_id':'61',
    }
    return context

def GetCoarchReport(request,params):
    params['report_name'] = 'laporan pelatihan karyawan (individu)'
    return params

def ConstructReport(response,params):
    response = CoachReport.reportIndividu(response,params)
    return response

actChoice = {'newCoach':newCoach,'GetCoarchReport':GetCoarchReport}
def GetContext(request,params):
    qf = params['action'].query_function
    context = actChoice[qf](request,params)
    return context
