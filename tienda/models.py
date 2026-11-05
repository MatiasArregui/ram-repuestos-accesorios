# from django.db import models

# # Create your models here.
# class Productos(models.Model):
    
#     categorias = [
#         ("Repuesto", "Repuesto"),
#         ("Accesorio", "Accesorio"),
#     ]
    
#     nombre = models.CharField(max_length=120)
#     precio = models.DecimalField(max_digits=12, decimal_places=2)
#     stock = models.IntegerField(default=0)
#     codigo = models.CharField(max_length=50, 
#                               unique=True)
#     categoria = models.CharField(max_length=10,
#                                  choices=categorias)
#     imagen_url = models.URLField(max_length=500, 
#                                  blank=True, 
#                                  null=True)
#     subCategoria = models.ForeignKey("SubCategoria", 
#                                      on_delete=models.PROTECT)

#     def __str__(self):
#         return self.nombre

# class SubCategoria(models.Model):
#     nombre = models.CharField(max_length=120, null=False)

#     def __str__(self):
#         return self.nombre
from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class SubCategoria(models.Model):

    CATEGORIAS = [
        ('Repuesto', 'Repuesto'),
        ('Accesorio', 'Accesorio'),
    ]

    nombre = models.CharField(max_length=120)

    categoria = models.CharField(
        max_length=10,
        choices=CATEGORIAS
    )

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    codigo = models.CharField(
        max_length=50,
        unique=True
    )

    nombre = models.CharField(max_length=120)

    marca = models.ForeignKey(
        Marca,
        on_delete=models.PROTECT
    )

    subcategoria = models.ForeignKey(
        SubCategoria,
        on_delete=models.PROTECT
    )

    precio = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    stock = models.IntegerField(
        default=0
    )

    imagen_url = models.URLField(
        max_length=500,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nombre