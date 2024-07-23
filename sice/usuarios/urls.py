from django.contrib import admin
from django.urls import path
from usuarios import views


urlpatterns = [
    path("",views.homeUsuarios,name="usuariosHome"),
]
