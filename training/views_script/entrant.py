from training.models import Entrant
from training.forms import fEntrant,fEntrantEdit
from django.db import transaction,IntegrityError
from django.shortcuts import get_object_or_404

def GetEntrant():
    entrant = Entrant.objects.all()#.filter(status_active=True)
    entrant = {'entrant':entrant,
        'action_id' : '2',
    }
    return entrant

def newEnt(request,params):
    msg = {}
    form = (fEntrant(),)
    if request.method == 'POST':
        cekform1 = fEntrant(request.POST)
        if cekform1.is_valid():
            try:
                with transaction.atomic():
                    entrant = cekform1.save()
                    msg = 'Berhasil menambahkan %s'%(entrant.member.person.name,)
            except IntegrityError:
                form = (cekform1,)
                msg = 'Gagal menambah data peserta'
    context = {
        'msg':msg,'form':form,'button':('Simpan',),'action':params['action'],
    }
    return context

def editEnt(request,params):
    p = params
    entrant = get_object_or_404(Entrant,pk=p['params'])
    msg = {}
    form = (fEntrant(instance=entrant),)
    if request.method == 'POST':
        cekform1 = fEntrant(request.POST or None, instance=entrant)
        if cekform1.is_valid() :
            members = cekform1.save()
            form = (cekform1,)
            msg = 'Sukses mengubah data %s'%(members.member.person.name,)

    context = {
        'msg':msg,'form':form,'button':('Ubah',),'action':p['action'],
    }
    return context

actChoice = {'+New':newEnt,'edit':editEnt}
def GetContext(request,params):
    action_name = params['action'].action_name
    context = actChoice[action_name](request,params)
    return context
