from django.db import models
from django.utils.timezone import datetime
from Pagina.choices import TIPO_CASAS
from Pagina.choices import ESTADO_PERRO
from Pagina.choices import LIST_REGION
from Pagina.choices import LIST_COMUNA

class Persona(models.Model):
    Rut = models.CharField(max_length=12)
    Nombre = models.CharField(max_length=30)
    Correo = models.CharField(max_length=50)
    Telefono = models.IntegerField()
    Tipo_casa = models.IntegerField(choices=TIPO_CASAS, default=1)
    Region = models.IntegerField(choices=LIST_REGION, default=1)
    Comuna = models.IntegerField(choices=LIST_COMUNA, default=1)
    Fecha_nacimiento = models.DateField(default=datetime.now)



class Perro(models.Model):
    Nombre = models.CharField(max_length=30)
    Raza = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=150)
    Imagen = models.ImageField(upload_to='photos', blank=True)
    Estado = models.IntegerField(choices=ESTADO_PERRO, default=2)

