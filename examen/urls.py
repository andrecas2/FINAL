from django.conf.urls import include, url

from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^estudiante/nuevo/$', views.estudiante_nuevo, name='estudiante_nuevo'),
    url(r'^grado/nuevo/$', views.grado_nuevo, name='grado_nuevo'),
]
