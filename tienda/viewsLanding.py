from django.shortcuts import render
from django.urls import reverse_lazy
from .models import SubCategoria, Producto, Marca
from .forms import ProductoForm, SubcategoriaForm, MarcaForm
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, TemplateView, DetailView
import random
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
# Pagina principal ----------------------------------------------------------------------------------->
def principal(request):
    productosId = [x.pk for x in Producto.objects.all()]
    producto_aleratorios = []
    try: 
        for x in range(16):
            producto_aleratorios.append(random.choice(productosId))
        productos = [{"pk":x.pk, "nombre":x.nombre, "imagen_mostrar":convertir_url_drive(x.imagen_url), "precio":x.precio} for x in Producto.objects.all() if x.pk in producto_aleratorios]
        context={"productos": productos}
    except:
        for x in range(2):
            producto_aleratorios.append(random.choice(productosId))
        productos = [{"pk":x.pk, "nombre":x.nombre, "imagen_mostrar":convertir_url_drive(x.imagen_url), "precio":x.precio} for x in Producto.objects.all() if x.pk in producto_aleratorios]
        context={"productos": productos}

    
    return render(request, os.path.join("landingPage", "pages", "principal.html"), context=context)


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

def listaProductos(request):
    
    productos = [{"pk":x.pk, "nombre":x.nombre, "imagen_mostrar":convertir_url_drive(x.imagen_url), "precio":x.precio, "subcategoria": x.subcategoria.nombre} for x in Producto.objects.all() if x.subcategoria.categoria == "Repuesto"]
    print(productos)
    productosCarrousel = []
    listaNros = []
    cantidad = len(productos)
    while len(listaNros) < 6:
        nroAzar = random.randint(0,cantidad-1)
        if nroAzar not in listaNros:
            listaNros.append(nroAzar)
            productosCarrousel.append(productos[nroAzar])
        else:
            print("ya existe en la lista")
        
    context={"productos": productos, "productosCarrousel": productosCarrousel}
    return render(request, os.path.join("landingPage", "pages", "productos.html"), context=context)

def listaAccesorios(request):
    
    accesorios = [{"pk":x.pk, "nombre":x.nombre, "imagen_mostrar":convertir_url_drive(x.imagen_url), "precio":x.precio, "subcategoria": x.subcategoria.nombre} for x in Producto.objects.all() if x.subcategoria.categoria == "Accesorio"]
    print(accesorios)
    accesoriosCarrousel = []
    listaNros = []
    cantidad = len(accesorios)
    while len(listaNros) < 6:
        nroAzar = random.randint(0,cantidad-1)
        if nroAzar not in listaNros:
            listaNros.append(nroAzar)
            accesoriosCarrousel.append(accesorios[nroAzar])
        else:
            print("ya existe en la lista")
        
    context={"accesorios": accesorios, "accesoriosCarrousel": accesoriosCarrousel}
    return render(request, os.path.join("landingPage", "pages", "accesorios.html"), context=context)


