from django.shortcuts import render
from django.urls import reverse_lazy
from .models import SubCategoria, Producto, Marca
from .forms import ProductoForm, SubcategoriaForm, MarcaForm
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, TemplateView, DetailView

import os
import re
from urllib.parse import urlparse, parse_qs

# ==========================================
# CONVERSIÓN DE URL DE GOOGLE DRIVE
# ==========================================

def convertir_url_drive(url):

    if not url:
        return ""

    url = url.strip()

    dominio = urlparse(url).hostname

    # Verificamos que sea un enlace de Google Drive
    if dominio not in ("drive.google.com", "www.drive.google.com"):
        return url

    # Extraemos el ID de la imagen
    coincidencia = re.search(r"/file/d/([^/]+)", url)

    if coincidencia:
        imagen_id = coincidencia.group(1)

    else:
        parametros = parse_qs(urlparse(url).query)
        imagen_id = parametros.get("id", [None])[0]

    # Generamos la nueva URL
    if imagen_id:
        return f"https://drive.google.com/thumbnail?id={imagen_id}&sz=w1000"

    return url


# ==========================================
# LISTADO DE PRODUCTOS
# ==========================================

class ProductosLista(ListView):

    model = Producto

    template_name = os.path.join(
        "landingPage", "pages", "principal.html"
    )

    context_object_name = 'productos'

    # paginate_by = 7

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # Convertimos las URL de las imágenes
        for producto in context['productos']:

            producto.imagen_mostrar = convertir_url_drive(
                producto.imagen_url
            )

        return context


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

        # Convertimos la URL de la imagen
        producto.imagen_mostrar = convertir_url_drive(
            producto.imagen_url
        )

        return context





