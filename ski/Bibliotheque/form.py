from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class LivreForm(ModelForm):
    class Meta:
        model = models.Livre
        fields = ('station', 'hotel', 'equipement', 'forfait','reservation')
        labels = {
            'station' : _('station'),
            'hotel' : _('hotel') ,
            'equipement' : _('equipement'),
            'forfait' : _('forfait'),
            'reservation' : _('reservation')
        }