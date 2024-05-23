from django import forms
from .models import CafeteriaCrous

class CafeteriaCrousForm(forms.ModelForm):
    class Meta:
        model = CafeteriaCrous
        fields = '__all__'
        widgets = {
            'menu': forms.CheckboxSelectMultiple,
        }
