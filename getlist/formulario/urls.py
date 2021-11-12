from django.urls import path

from formulario import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente', views.formulario, name='formulario'),

]