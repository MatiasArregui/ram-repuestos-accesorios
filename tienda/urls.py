from django.contrib import admin
from django.urls import path
from . import views, viewsLanding
# from .forms import LoginForm
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    # path('', views.listadatos, name='listadatos'),
    path("manage/", views.InicioView.as_view(), name="inicio"),
    # Productos URLs--------------------------------------------------------------------------------->
    path("manage/productos/", views.ListaProductos.as_view(), name="listaProductos"),
    path("manage/productos/nuevo", views.ProductoCreateView.as_view(), name="nuevoProducto"),
    path("manage/productos/modificar/<str:pk>", views.ProductoUpdateView.as_view(), name="modificarProducto"),
    path("manage/productos/borrar/<str:pk>", views.ProductoDeleteView.as_view(), name="borrarProducto"),

    # Subcategorias URLs--------------------------------------------------------------------------------->
    path("manage/subcategorias/", views.ListaSubcategorias.as_view(), name="listaSubcategorias"),
    path("manage/subcategorias/nuevo", views.SubcategoriaCreateView.as_view(), name="nuevaSubcategoria"),
    path("manage/subcategorias/modificar/<str:pk>", views.SubcategoriaUpdateView.as_view(), name="modificarSubcategoria"),
    path("manage/subcategorias/borrar/<str:pk>", views.SubcategoriaDeleteView.as_view(), name="borrarSubcategoria"),
    
    # Marcas URLs--------------------------------------------------------------------------------->
    path("manage/marcas/", views.ListaMarcas.as_view(), name="listaMarcas"),
    path("manage/marcas/nuevo", views.MarcaCreateView.as_view(), name="nuevaMarca"),
    path("manage/marcas/modificar/<str:pk>", views.MarcaUpdateView.as_view(), name="modificarMarca"),
    path("manage/marcas/borrar/<str:pk>", views.MarcaDeleteView.as_view(), name="borrarMarca"),
    
    
    # Landing page URLs--------------------------------------------------------------------------------->
    path("", viewsLanding.principal, name="principalLanding"),
    # path("productos/", viewsLanding.ProductosLista.as_view(), name="productoLista"),
    path("accesorios/", viewsLanding.listaAccesorios, name="accesorioLista"),
    path("productos/", viewsLanding.listaProductos, name="productoLista"),
    path("detalle/<str:pk>", viewsLanding.DetalleProducto.as_view(), name="detalleProducto"),
]
