from django.contrib import admin
from django.urls import path
from catalogos import views


urlpatterns = [
    path("",views.homeCatalogos,name="catalogosHome"),
]
