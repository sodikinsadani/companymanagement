from ..models import Person,Action,Employee
from ..forms import fEmployee,fPerson
from django.db import transaction,IntegrityError
from django.shortcuts import get_object_or_404

def GetEmloyees():
    employee = Employee.objects.all()
    employee = {'employee':employee,
        'action_id' : '2',
    }
    return employee

def editEmp(request,params):
    p = params
    employee = get_object_or_404(Employee,pk=p['params'])
    msg = {}
    form = (fPerson(instance=employee.person),fEmployee(instance=employee))
    if request.method == 'POST':
        cekform1 = fPerson(request.POST or None, instance=employee.person)
        cekform2 = fEmployee(request.POST or None, instance=employee)
        if cekform1.is_valid() and cekform2.is_valid():
            try:
                with transaction.atomic():
                    person = cekform1.save()
                    cekform2.save()
                    form = (cekform1,cekform2)
                    msg = 'Sukses mengubah data %s dengan ID %s'%(person.name,person.id)
            except IntegrityError:
                handle_exception()

    context = {
        'msg':msg,'form':form,'button':('Ubah',),'action':p['action'],
    }
    return context

def newEmp(request,params):
    msg = {}
    form = (fPerson(),fEmployee())
    if request.method == 'POST':
        cekform1 = fPerson(request.POST)
        cekform2 = fEmployee(request.POST)
        if cekform1.is_valid() and cekform2.is_valid():
            try:
                with transaction.atomic():
                    person = cekform1.save()
                    employee = cekform2.save(commit=False)
                    employee.person = person
                    employee.save()
                    msg = 'Berhasil menambahkan %s dengan ID %s'%(person.name,person.id)
            except IntegrityError:
                form = (cekform1,cekform2)
                msg = 'Gagal menambah data karyawan'
    context = {
        'msg':msg,'form':form,'button':('Simpan',),'action':params['action'],
    }
    return context

actChoice = {'+New':newEmp,'edit':editEmp}
def GetContext(request,params):
    action_name = params['action'].action_name
    context = actChoice[action_name](request,params)
    return context
