from django import forms
from plat.models import Plat



class PlatForm(forms.ModelForm):
    class Meta:
        model = Plat
        fields = [
            'name',
            'summary'
        ]