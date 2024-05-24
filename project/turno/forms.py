from django import forms

from . import models

class TurnoLugarForm(forms.ModelForm):
    class Meta:
        model = models.TurnoLugar
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }
        
class TurnoForm(forms.ModelForm):
    class Meta:
        model = models.Turno
        fields = "__all__"       
        

