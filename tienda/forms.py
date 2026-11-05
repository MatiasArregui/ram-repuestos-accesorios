from django import forms
from .models import SubCategoria, Producto, Marca
from django.forms import inlineformset_factory
from django.contrib.auth.forms import AuthenticationForm


#FORMULARIO DE PRODUCTOS (CREAR Y MODIFICAR)
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ("codigo", "nombre", "marca", "subcategoria",
                  "precio", "stock", "imagen_url")
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'marca':  forms.Select(attrs={'class':'form-control'}),
            "subcategoria":  forms.Select(attrs={'class':'form-control'}),
            "precio": forms.NumberInput(attrs={"class": "form-control"}),
            "stock": forms.NumberInput(attrs={"class": "form-control"}),
            "imagen_url" : forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL del PDF'}),
        }
        labels = {
            "codigo":"Código ",
            "nombre":"Nombre",
            "marca":"Marca",
            "subcategoria":"subCategoria",
            "precio":"Precio",
            "stock":"Stock",
            "imagen_url":"URL de la imagen",
        }
        

#FORMULARIO DE SUBCATEGORIAS (CREAR Y MODIFICAR)
class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model = SubCategoria
        fields = ("nombre", "categoria")
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            "nombre":"Nombre",
            "categoria":"categoria",
        }


#FORMULARIO DE SUBCATEGORIAS (CREAR Y MODIFICAR)
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ("nombre",)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            "nombre":"Nombre",
        }