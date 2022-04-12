from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    pub_date = models.DateField('date published')

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.nombre

class Cliente(models.Model):
      nombres = models.CharField(max_length=50)
      apellidos = models.CharField(max_length=50)
      dni =models.IntegerField
      fecha_nacimiento=models.DateField('nacimiento')
      fecha_publicacion = models.DateField('date published')

      def __str__(self) -> str:
          return self.nombres +" "+ self.apellidos
