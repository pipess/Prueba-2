from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.Index, name='Home'),
        url(r'^quienes.html/$', views.quienes, name='QuienesSomos'),
        url(r'^registro.html/$', views.registro, name='Registro'),
        url(r'^contacto.html/$', views.contacto, name='Contacto'),
        url(r'^regPerro.html/$', views.regPerro, name='regPerro'),
        url(r'^perro_list.html/$', views.perro_list, name='listado'),
    	]
