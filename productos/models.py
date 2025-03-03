from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    foto = models.ImageField(upload_to='productos/')
    fecha_creacion = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.nombre
    
class CarritoItem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    sesion_id = models.CharField(max_length=100, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
    
    def subtotal(self):
        return self.producto.precio * self.cantidad

    
   
#pasarela decompras



class Orden(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    sesion_id = models.CharField(max_length=100, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=0)
    metodo_pago = models.CharField(
        max_length=20,
        choices=[('nequi', 'Nequi'), ('bancolombia', 'Bancolombia')]
    )
    pagado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden #{self.id} - {self.nombre}"

class OrdenItem(models.Model):
    orden = models.ForeignKey(Orden, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey("Producto", on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

    def subtotal(self):
        return self.precio * self.cantidad

class Datos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    otro_campo = models.CharField(max_length=100)



