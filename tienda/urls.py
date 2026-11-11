
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views, viewsLanding

urlpatterns = [

    # PANEL PRINCIPAL
    path(
        "manage/",
        login_required(views.InicioView.as_view()),
        name="inicio"
    ),

    # PRODUCTOS
    path(
        "manage/productos/",
        login_required(views.ListaProductos.as_view()),
        name="listaProductos"
    ),

    path(
        "manage/productos/nuevo",
        login_required(views.ProductoCreateView.as_view()),
        name="nuevoProducto"
    ),

    path(
        "manage/productos/modificar/<str:pk>",
        login_required(views.ProductoUpdateView.as_view()),
        name="modificarProducto"
    ),

    path(
        "manage/productos/borrar/<str:pk>",
        login_required(views.ProductoDeleteView.as_view()),
        name="borrarProducto"
    ),

    # SUBCATEGORÍAS
    path(
        "manage/subcategorias/",
        login_required(views.ListaSubcategorias.as_view()),
        name="listaSubcategorias"
    ),

    path(
        "manage/subcategorias/nuevo",
        login_required(views.SubcategoriaCreateView.as_view()),
        name="nuevaSubcategoria"
    ),

    path(
        "manage/subcategorias/modificar/<str:pk>",
        login_required(views.SubcategoriaUpdateView.as_view()),
        name="modificarSubcategoria"
    ),

    path(
        "manage/subcategorias/borrar/<str:pk>",
        login_required(views.SubcategoriaDeleteView.as_view()),
        name="borrarSubcategoria"
    ),

    # MARCAS
    path(
        "manage/marcas/",
        login_required(views.ListaMarcas.as_view()),
        name="listaMarcas"
    ),

    path(
        "manage/marcas/nuevo",
        login_required(views.MarcaCreateView.as_view()),
        name="nuevaMarca"
    ),

    path(
        "manage/marcas/modificar/<str:pk>",
        login_required(views.MarcaUpdateView.as_view()),
        name="modificarMarca"
    ),

    path(
        "manage/marcas/borrar/<str:pk>",
        login_required(views.MarcaDeleteView.as_view()),
        name="borrarMarca"
    ),

    # LANDING PAGE
    path("", viewsLanding.principal, name="principalLanding"),

    path(
        "detailing/",
        viewsLanding.listaDetailing,
        name="detailingLista"
    ),

    path(
        "accesorios/",
        viewsLanding.listaAccesorios,
        name="accesorioLista"
    ),

    path(
        "productos/",
        viewsLanding.listaProductos,
        name="productoLista"
    ),

    path(
        "detalle/<str:pk>",
        viewsLanding.DetalleProducto.as_view(),
        name="detalleProducto"
    ),
    
    # URLS DEL CARRITO

    path(
        'carrito/',
        viewsLanding.verCarrito,
        name='verCarrito'
    ),

    path(
        'carrito/agregar/<str:pk>/',
        viewsLanding.agregarCarrito,
        name='agregarCarrito'
    ),

    path(
        'carrito/actualizar/<str:pk>/',
        viewsLanding.actualizarCarrito,
        name='actualizarCarrito'
    ),

    path(
        'carrito/eliminar/<str:pk>/',
        viewsLanding.eliminarCarrito,
        name='eliminarCarrito'
    ),

    path(
        'carrito/whatsapp/',
        viewsLanding.solicitarWhatsApp,
        name='solicitarWhatsApp'
    ),


]
