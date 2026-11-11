
import os
import random
import re

from decimal import Decimal
from urllib.parse import urlparse, parse_qs, quote

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import DetailView
from django.views.decorators.http import require_POST
from django.utils.http import url_has_allowed_host_and_scheme

from .models import SubCategoria, Producto


# ==========================================
# CONVERSIÓN DE URL DE GOOGLE DRIVE
# ==========================================

def convertir_url_drive(url):

    if not url:
        return ""

    url = url.strip()

    dominio = urlparse(url).hostname

    if dominio not in ("drive.google.com", "www.drive.google.com"):
        return url

    coincidencia = re.search(r"/file/d/([^/]+)", url)

    if coincidencia:
        imagen_id = coincidencia.group(1)

    else:
        parametros = parse_qs(urlparse(url).query)
        imagen_id = parametros.get("id", [None])[0]

    if imagen_id:
        return f"https://drive.google.com/thumbnail?id={imagen_id}&sz=w1000"

    return url


# ==========================================
# FUNCIONES AUXILIARES
# ==========================================

def obtener_productos_aleatorios(productos, cantidad=6):

    return random.sample(
        productos,
        min(cantidad, len(productos))
    )


def obtener_carrito(request):

    carrito = request.session.get('carrito', {})

    if not isinstance(carrito, dict):
        carrito = {}

    carrito_limpio = {}

    for producto_id, cantidad in carrito.items():

        try:
            producto_id = str(int(producto_id))
            cantidad = int(cantidad)

            if cantidad > 0:
                carrito_limpio[producto_id] = cantidad

        except (ValueError, TypeError):
            continue

    request.session['carrito'] = carrito_limpio

    return carrito_limpio


def volver_a_pagina_anterior(request):

    referer = request.META.get('HTTP_REFERER', '')

    if url_has_allowed_host_and_scheme(
        referer,
        allowed_hosts={request.get_host()}
    ):
        return redirect(referer)

    return redirect('verCarrito')


# ==========================================
# PÁGINA PRINCIPAL
# ==========================================

def principal(request):

    productos_db = list(Producto.objects.all())

    productos_seleccionados = obtener_productos_aleatorios(
        productos_db,
        20
    )

    productos = [
        {
            "pk": p.pk,
            "nombre": p.nombre,
            "imagen_mostrar": convertir_url_drive(p.imagen_url),
            "precio": p.precio
        }
        for p in productos_seleccionados
    ]

    context = {
        "productos": productos
    }

    return render(
        request,
        os.path.join("landingPage", "pages", "principal.html"),
        context
    )


# ==========================================
# DETALLE DE PRODUCTO
# ==========================================

class DetalleProducto(DetailView):

    model = Producto

    template_name = os.path.join(
        "landingPage", "pages", "productoDetalle.html"
    )

    context_object_name = 'producto'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        producto = context['producto']

        producto.imagen_mostrar = convertir_url_drive(
            producto.imagen_url
        )

        return context


# ==========================================
# LISTADO DE PRODUCTOS
# ==========================================

def listaProductos(request):

    productos = [
        {
            "pk": p.pk,
            "nombre": p.nombre,
            "imagen_mostrar": convertir_url_drive(p.imagen_url),
            "precio": p.precio,
            "subcategoria": p.subcategoria.nombre
        }
        for p in Producto.objects.select_related(
            'subcategoria'
        ).filter(subcategoria__categoria="Repuesto")
    ]

    productosCarrousel = obtener_productos_aleatorios(
        productos,
        6
    )

    context = {
        "productos": productos,
        "productosCarrousel": productosCarrousel
    }

    return render(
        request,
        os.path.join("landingPage", "pages", "productos.html"),
        context
    )


def listaAccesorios(request):

    accesorios = [
        {
            "pk": p.pk,
            "nombre": p.nombre,
            "imagen_mostrar": convertir_url_drive(p.imagen_url),
            "precio": p.precio,
            "subcategoria": p.subcategoria.nombre
        }
        for p in Producto.objects.select_related(
            'subcategoria'
        ).filter(subcategoria__categoria="Accesorio")
    ]

    accesoriosCarrousel = obtener_productos_aleatorios(
        accesorios,
        6
    )

    context = {
        "accesorios": accesorios,
        "accesoriosCarrousel": accesoriosCarrousel
    }

    return render(
        request,
        os.path.join("landingPage", "pages", "accesorios.html"),
        context
    )


def listaDetailing(request):

    elementos = [
        {
            "pk": p.pk,
            "nombre": p.nombre,
            "imagen_mostrar": convertir_url_drive(p.imagen_url),
            "precio": p.precio,
            "subcategoria": p.subcategoria.nombre
        }
        for p in Producto.objects.select_related(
            'subcategoria'
        ).filter(subcategoria__categoria="Detailing")
    ]

    elementosCarrousel = obtener_productos_aleatorios(
        elementos,
        6
    )

    context = {
        "elementos": elementos,
        "elementosCarrousel": elementosCarrousel
    }

    return render(
        request,
        os.path.join("landingPage", "pages", "detailing.html"),
        context
    )


# ==========================================
# AGREGAR PRODUCTO AL CARRITO
# ==========================================

@require_POST
def agregarCarrito(request, pk):

    producto = get_object_or_404(Producto, pk=pk)

    carrito = obtener_carrito(request)

    producto_id = str(producto.pk)

    cantidad_actual = carrito.get(producto_id, 0)

    if producto.stock <= 0:

        messages.warning(
            request,
            f"{producto.nombre} no tiene stock disponible."
        )

        return volver_a_pagina_anterior(request)

    if cantidad_actual >= producto.stock:

        messages.warning(
            request,
            f"Solo hay {producto.stock} unidades disponibles de {producto.nombre}."
        )

        return volver_a_pagina_anterior(request)

    carrito[producto_id] = cantidad_actual + 1

    request.session['carrito'] = carrito

    messages.success(
        request,
        f"{producto.nombre} se agregó al carrito."
    )

    return volver_a_pagina_anterior(request)


# ==========================================
# MOSTRAR CARRITO
# ==========================================

def verCarrito(request):

    carrito = obtener_carrito(request)

    productos_db = Producto.objects.filter(
        pk__in=carrito.keys()
    ).select_related('marca')

    productos_dict = {
        str(p.pk): p
        for p in productos_db
    }

    productos = []
    total = Decimal('0.00')

    for producto_id, cantidad in carrito.items():

        producto = productos_dict.get(producto_id)

        if not producto:
            continue

        subtotal = producto.precio * cantidad

        producto.imagen_mostrar = convertir_url_drive(
            producto.imagen_url
        )

        productos.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

        total += subtotal

    cantidadTotal = sum(
        item['cantidad']
        for item in productos
    )

    context = {
        'productos': productos,
        'total': total,
        'cantidadTotal': cantidadTotal
    }

    return render(
        request,
        os.path.join("landingPage", "pages", "carrito.html"),
        context
    )


# ==========================================
# ACTUALIZAR CANTIDAD
# ==========================================

@require_POST
def actualizarCarrito(request, pk):

    producto = get_object_or_404(Producto, pk=pk)

    carrito = obtener_carrito(request)

    producto_id = str(producto.pk)

    if producto_id not in carrito:
        return redirect('verCarrito')

    try:
        cantidad = int(request.POST.get('cantidad', 1))

    except (ValueError, TypeError):

        messages.error(
            request,
            "La cantidad ingresada no es válida."
        )

        return redirect('verCarrito')

    if cantidad < 1:

        messages.warning(
            request,
            "La cantidad debe ser como mínimo 1."
        )

    elif cantidad > producto.stock:

        messages.warning(
            request,
            f"Solo hay {producto.stock} unidades disponibles."
        )

    else:

        carrito[producto_id] = cantidad

        request.session['carrito'] = carrito

        messages.success(
            request,
            "Cantidad actualizada correctamente."
        )

    return redirect('verCarrito')


# ==========================================
# ELIMINAR PRODUCTO DEL CARRITO
# ==========================================

@require_POST
def eliminarCarrito(request, pk):

    carrito = obtener_carrito(request)

    carrito.pop(str(pk), None)

    request.session['carrito'] = carrito

    messages.success(
        request,
        "Producto eliminado del carrito."
    )

    return redirect('verCarrito')


# ==========================================
# SOLICITAR PEDIDO POR WHATSAPP
# ==========================================

def solicitarWhatsApp(request):

    carrito = obtener_carrito(request)

    if not carrito:

        messages.warning(
            request,
            "Tu carrito está vacío."
        )

        return redirect('verCarrito')

    productos_db = Producto.objects.filter(
        pk__in=carrito.keys()
    ).select_related('marca')

    productos_dict = {
        str(p.pk): p
        for p in productos_db
    }

    mensaje = (
        "¡Hola! Quisiera solicitar los siguientes productos:\n\n"
    )

    total = Decimal('0.00')

    for producto_id, cantidad in carrito.items():

        producto = productos_dict.get(producto_id)

        if not producto:

            messages.warning(
                request,
                "Uno de los productos ya no está disponible."
            )

            return redirect('verCarrito')

        if cantidad > producto.stock:

            messages.warning(
                request,
                f"Stock insuficiente para {producto.nombre}. "
                f"Disponibles: {producto.stock}."
            )

            return redirect('verCarrito')

        subtotal = producto.precio * cantidad

        total += subtotal

        mensaje += (
            f"Producto: {producto.nombre}\n"
            f"Código: {producto.codigo}\n"
            f"Marca: {producto.marca.nombre}\n"
            f"Cantidad: {cantidad}\n"
            f"Precio unitario: ${producto.precio}\n"
            f"Subtotal: ${subtotal}\n\n"
        )

    mensaje += f"TOTAL ESTIMADO: ${total}\n\n"

    mensaje += (
        "¿Podrían confirmarme la disponibilidad "
        "y las condiciones del pedido?"
    )

    # REEMPLAZAR POR EL NÚMERO REAL DE WHATSAPP
    numero = "+5493544644455"

    url = f"https://wa.me/{numero}?text={quote(mensaje)}"

    return redirect(url)

