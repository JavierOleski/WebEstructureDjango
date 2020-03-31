from django import forms

from .models import Ficha_basica

class Form_ficha_basica(forms.ModelForm):
    class Meta:
        model   = Ficha_basica
        fields  = [
            'nombre',
            'dni',
            'edad'
        ]