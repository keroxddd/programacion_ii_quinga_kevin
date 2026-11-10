from django.db import models

from .categoria import Categoria


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='libros',
    )
    isbn = models.CharField(max_length=17, unique=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']
