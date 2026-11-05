from django.shortcuts import render
from django.urls import reverse_lazy
from .models import SubCategoria, Producto, Marca
from .forms import ProductoForm, SubcategoriaForm
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
import os



# Create your views here.
class ListaProductos(ListView):
    model = Producto
    template_name = os.path.join("listas", "listaProductos.html")
    context_object_name = 'Producto'
    #Sacamos la paginacion para que nos permita usar los datos presentes en el template
    # paginate_by = 7
    
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name =  os.path.join("forms", "productoFormulario.html")
    success_url = reverse_lazy('listaProductos')
    
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = os.path.join("forms", "productoFormulario.html")
    success_url = reverse_lazy('listaProductos')
    
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/eliminarProducto.html'
    success_url = reverse_lazy('listaProductos')
    
    
# <------------------------------------------>
# Create your views here.
class ListaSubcategorias(ListView):
    model = SubCategoria
    template_name = os.path.join("listas", "listaSubcategorias.html")
    context_object_name = 'subcategoria'
    #Sacamos la paginacion para que nos permita usar los datos presentes en el template
    # paginate_by = 7
    
class SubcategoriaCreateView(CreateView):
    model = SubCategoria
    form_class = SubcategoriaForm
    template_name =  os.path.join("forms", "subcategoriaFormulario.html")
    success_url = reverse_lazy('listaSubcategorias')
    
class SubcategoriaUpdateView(UpdateView):
    model = SubCategoria
    form_class = SubcategoriaForm
    template_name =  os.path.join("forms", "subcategoriaFormulario.html")
    success_url = reverse_lazy('listaSubcategorias')
    
class SubcategoriaDeleteView(DeleteView):
    model = Producto
    template_name = 'Subcategorias/eliminarSubcategoria.html'
    success_url = reverse_lazy('listaSubcategorias')
    
    