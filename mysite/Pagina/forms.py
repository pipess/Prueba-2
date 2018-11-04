from django import forms
from .models import Persona
from .models import Perro
from Pagina.choices import TIPO_CASAS
from Pagina.choices import ESTADO_PERRO
from Pagina.choices import LIST_REGION
from Pagina.choices import LIST_COMUNA

class Registro(forms.Form):
    Rut = forms.CharField()
    Nombre = forms.CharField()
    Correo = forms.EmailField()
    Telefono = forms.IntegerField()
    Fecha_nacimiento = forms.DateField()
    Tipo_casa = forms.ChoiceField(choices = TIPO_CASAS, widget=forms.Select())
    Region = forms.ChoiceField(choices = LIST_REGION, widget=forms.Select())
    Comuna = forms.ChoiceField(choices = LIST_COMUNA, widget=forms.Select())

class rePerro(forms.Form):

    Nombre = forms.CharField()
    Raza = forms.CharField()
    Descripcion = forms.CharField(widget=forms.Textarea)
    Estado = forms.ChoiceField(choices = ESTADO_PERRO, widget=forms.Select())