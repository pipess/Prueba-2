from django.shortcuts import render
from Pagina.models import Persona
from Pagina.models import Perro
from Pagina.forms import Registro
from Pagina.forms import rePerro 
from Pagina.choices import TIPO_CASAS
from Pagina.choices import ESTADO_PERRO
from Pagina.choices import LIST_REGION
from Pagina.choices import LIST_COMUNA



# Create your views here.
def Index(request):
    return render(request, 'Pagina/Index.html', {})

def quienes(request):
    return render(request, 'Pagina/quienes.html', {})

def registro(request):
    form_registro = Registro(request.POST or None)
    variables = {
        "form":form_registro
    }
    if form_registro.is_valid():
       datos = form_registro.cleaned_data
       Rut = datos.get("Rut")
       Nombre = datos.get("Nombre")
       Correo = datos.get("Correo")
       Telefono = datos.get("Telefono") 
       Fecha_nacimiento = datos.get("Fecha_nacimiento")
       Tipo_casa = datos.get("Tipo_casa")
       Region = datos.get("Region") 
       Comuna = datos.get("Comuna") 
       db_registro = Persona(Rut=Rut, Nombre=Nombre, Correo=Correo, Telefono=Telefono, Tipo_casa=Tipo_casa, Region=Region, Comuna=Comuna, Fecha_nacimiento=Fecha_nacimiento)
       db_registro.save()
    return render(request, 'Pagina/registro.html', variables )    

def contacto(request):
    return render(request, 'Pagina/contacto.html', {})    

def regPerro(request):
    form_rePerro = rePerro(request.POST or None)
    variabl = {
        "form":form_rePerro
    }
    if form_rePerro.is_valid():
       datos = form_rePerro.cleaned_data
       Nombre = datos.get("Nombre")
       Raza = datos.get("Raza")
       Descripcion = datos.get("Descripcion")
       Estado = datos.get("Estado") 
      
       db_rePerro = Perro(Nombre=Nombre, Raza=Raza, Descripcion=Descripcion, Estado=Estado)
       db_rePerro.save()
    return render(request, 'Pagina/regPerro.html', variabl )  

def perro_list(request):
    perro = Perro.objects.all()
    context = {'perros':perro}
    return render(request, 'Pagina/perro_list.html', context)  

def delPerro(request, id_perro):
    perro = Perro.objects.get(id=id_mascota)
    if request.method =='GET':
        form = rePerro(instance=perro)
    else:
        form = rePerro(request.POST, instance=perro)
        if form.is_valid():
            form.save()    
    return render(request, 'Pagina/contacto.html', {'form':form})    



