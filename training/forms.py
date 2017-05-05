from django import forms
from .models import Entrant
from django.utils.translation import ugettext_lazy as _

class DateInput(forms.DateInput):
    input_type = 'date'

class fEntrant(forms.ModelForm):
    class Meta:
        model = Entrant
        exclude = ['date_input',]
        widgets = {
        }
        labels = {
            'member': _('Peserta'),
            'status_active': _('Status Aktif'),
            'description': _('Keterangan'),
        }

class fEntrantEdit(forms.ModelForm):
    class Meta:
        model = Entrant
        exclude = ['date_input','member']
        widgets = {
        }
        labels = {
            'status_active': _('Status Aktif'),
            'description': _('Keterangan'),
        }
