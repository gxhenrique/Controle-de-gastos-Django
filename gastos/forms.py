from django import forms

from .models import financaModel

class FormsModel(forms.ModelForm):
    class Meta:
        model = financaModel
        fields = ['titulo', 'valor', 'tipo']