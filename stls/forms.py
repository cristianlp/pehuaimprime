from django import forms
from .models import Stl

class StlForm(forms.ModelForm):
    class Meta:
        model = Stl
        fields = ('nombre', 'archivo')