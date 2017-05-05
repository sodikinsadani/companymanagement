from django import forms
from .models import Person,Employee,Coaching
from django.utils.translation import ugettext_lazy as _

class DateInput(forms.DateInput):
    input_type = 'date'

class fEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['person','date_input',]
        widgets = {
            'date_register':DateInput(),
        }
        labels = {
            'grade': _('Level'),
            'date_register': _('Tanggal Daftar'),
            'status_active': _('Status'),
            'description': _('Keterangan'),
        }

class fPerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'birth':DateInput(),
        }
        labels = {
            'name': _('Nama'),
            'birthplace': _('Tempat Lahir'),
            'birth': _('Tanggal Lahir'),
            'gender': _('Jenis Kelamin'),
            'address': _('Alamat'),
            'status': _('Status Pernikahan'),
            'school': _('Sekolah'),
            'graduate': _('Jenjang Pendidikan'),
            'mobilephone': _('Handphone'),
        }

class fCoaching(forms.ModelForm):
    class Meta:
        model = Coaching
        exclude = ['employee']
        widgets = {
            'date_coaching':DateInput(),
        }
        labels = {
            'course':_('Materi Pelatihan'),
            'date_coaching':_('Tanggal Pelatihan'),
            'description':_('Keterangan'),
        }
