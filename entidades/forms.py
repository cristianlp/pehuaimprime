from django import forms
from .models import Entidad

class EntidadForm(forms.ModelForm):

    class Meta:
        model = Entidad
        fields = (
           'nombre', 'contacto',
        )

    #validar unicidad del nombre
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if (Entidad.objects.exclude(pk=self.instance.pk).filter(nombre__iexact=nombre).exists()):
            raise forms.ValidationError("El nombre de la entidad ingresada ya existe")
        
        return nombre
