from django.db import models

# Create your models here.
class lentes(models.Model):
    nombre = models.CharField(max_length=150, null=False)
    descripcion = models.CharField(max_length=800, null=False)
    imagenUrl = models.CharField(max_length=150, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    ispaypal = models.BooleanField(default=False)

    class Meta:
        db_table = 'lentes'
        verbose_name_plural = "Tabla info Lentes"

    def __str__(self):
        return self.nombre