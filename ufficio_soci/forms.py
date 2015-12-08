import datetime

import autocomplete_light
from django import forms

from anagrafica.models import Estensione


class ModuloCreazioneEstensione(autocomplete_light.ModelForm):
    class Meta:
        model = Estensione
        fields = ['persona', 'destinazione', ]


class ModuloElencoSoci(forms.Form):
    al_giorno = forms.DateField(help_text="La data alla quale generare l'elenco soci.",
                                required=True, initial=datetime.date.today)

    def clean_al_giorno(self):  # Non permette date passate
        al_giorno = self.cleaned_data['al_giorno']
        if al_giorno < datetime.date.today():
            raise forms.ValidationError("La data deve essere futura.")
        return al_giorno


class ModuloElencoElettorato(forms.Form):
    ELETTORATO_ATTIVO = 'A'
    ELETTORATO_PASSIVO = 'P'
    ELETTORATO = (
        (ELETTORATO_ATTIVO, "Attivo"),
        (ELETTORATO_PASSIVO, "Passivo"),
    )
    al_giorno = forms.DateField(help_text="La data delle elezioni.",
                                    required=True, initial=datetime.date.today)
    elettorato = forms.ChoiceField(choices=ELETTORATO, initial=ELETTORATO_PASSIVO)
