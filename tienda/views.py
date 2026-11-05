from django.shortcuts import render
from django.urls import reverse_lazy
from .models import SubCategoria, Producto, Marca
from .forms import ProductoForm, SubcategoriaForm, MarcaForm
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, TemplateView
import os


class InicioView(TemplateView):
    template_name = os.path.join("carga", "manage", "managePage.html")


# Create your views here.
class ListaProductos(ListView):
    model = Producto
    template_name = os.path.join("carga","listas", "listaProductos.html")
    context_object_name = 'Producto'
    #Sacamos la paginacion para que nos permita usar los datos presentes en el template
    # paginate_by = 7
    
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name =  os.path.join("carga", "forms", "productoFormulario.html")
    success_url = reverse_lazy('listaProductos')
    
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = os.path.join("carga","forms", "productoFormulario.html")
    success_url = reverse_lazy('listaProductos')
    
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = os.path.join("carga","borrar", "eliminarProducto.html")
    success_url = reverse_lazy('listaProductos')
    
    
# <------------------------------------------>
# Create your views here.
class ListaSubcategorias(ListView):
    model = SubCategoria
    template_name = os.path.join("carga","listas", "listaSubcategorias.html")
    context_object_name = 'subcategoria'
    #Sacamos la paginacion para que nos permita usar los datos presentes en el template
    # paginate_by = 7
    
class SubcategoriaCreateView(CreateView):
    model = SubCategoria
    form_class = SubcategoriaForm
    template_name =  os.path.join("carga","forms", "subcategoriaFormulario.html")
    success_url = reverse_lazy('listaSubcategorias')
    
class SubcategoriaUpdateView(UpdateView):
    model = SubCategoria
    form_class = SubcategoriaForm
    template_name =  os.path.join("carga","forms", "subcategoriaFormulario.html")
    success_url = reverse_lazy('listaSubcategorias')
    
class SubcategoriaDeleteView(DeleteView):
    model = SubCategoria
    template_name = os.path.join("carga","borrar", "eliminarSubcategoria.html")
    success_url = reverse_lazy('listaSubcategorias')
    








    
# <------------------------------------------>
# Create your views here.
class ListaMarcas(ListView):
    model = Marca
    template_name = os.path.join("carga","listas", "listaMarcas.html")
    context_object_name = 'marcas'
    #Sacamos la paginacion para que nos permita usar los datos presentes en el template
    # paginate_by = 7
    
class MarcaCreateView(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name =  os.path.join("carga","forms", "marcaFormulario.html")
    success_url = reverse_lazy('listaMarcas')
    
class MarcaUpdateView(UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name =  os.path.join("carga","forms", "marcaFormulario.html")
    success_url = reverse_lazy('listaMarcas')
    
class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = os.path.join("carga","borrar", "eliminarMarca.html")
    success_url = reverse_lazy('listaMarcas')
    
    