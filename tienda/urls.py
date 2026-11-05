from django.contrib import admin
from django.urls import path
from . import views
# from .forms import LoginForm
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    # path('', views.listadatos, name='listadatos'),
    # Productos URLs--------------------------------------------------------------------------------->
    path("productos/", views.ListaProductos.as_view(), name="listaProductos"),
    path("productos/nuevo", views.ProductoCreateView.as_view(), name="nuevoElemento"),
    path("productos/modificar/<str:pk>", views.ProductoUpdateView.as_view(), name="modificarElemento"),
    path("productos/borrar/<str:pk>", views.ProductoDeleteView.as_view(), name="borrarElemento"),

    # Personas URLs--------------------------------------------------------------------------------->
    path("subcategorias/", views.ListaSubcategorias.as_view(), name="listaSubcategorias"),
    path("subcategorias/nuevo", views.SubcategoriaCreateView.as_view(), name="nuevoElemento"),
    path("subcategorias/modificar/<str:pk>", views.SubcategoriaUpdateView.as_view(), name="modificarElemento"),
    path("subcategorias/borrar/<str:pk>", views.SubcategoriaDeleteView.as_view(), name="borrarElemento"),
]
