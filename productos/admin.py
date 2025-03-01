from django.contrib import admin
from .models import(Producto)
from django.contrib.admin.sites import AlreadyRegistered

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ('nombre', 'precio', 'fecha_creacion','foto')
    list_display_links = ('nombre',)

admin.site.register(Producto, ProductoAdmin)



from .models import CarritoItem
class CarritoItemAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'usuario', 'sesion_id', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('producto__nombre', 'usuario__username')

try:
    admin.site.register(CarritoItem, CarritoItemAdmin)
except AlreadyRegistered:
    pass
