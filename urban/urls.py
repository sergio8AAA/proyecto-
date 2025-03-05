from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

# Importamos todas las vistas de productos
from productos import views  

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Páginas principales
    path('', views.index, name='index'),  # Página principal
    path('home/', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('mapanoti/', views.mapanoti, name='mapanoti'),
    path('contactenos/', views.contactenos, name='contactenos'),


    # Autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Manteniendo solo una
    path('registro/', views.registro, name='registro'),
    path("accounts/login/", LoginView.as_view(template_name="login.html"), name="login"),

    # Tienda y productos
    path('tienda/', views.tienda, name='tienda'),
    path('productos/', views.productos, name='productos'),

    # Perfil de usuario
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('resetear/', views.resetear, name='resetear'),
    path('editar_perfil/<uidb64>/<token>/', views.editar_perfil, name="editar_perfil"),

    # Carrito de compras
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/actualizar/<int:item_id>/', views.actualizar_carrito, name='actualizar_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_item, name='eliminar_item'),

    # Pasarela de pagos y confirmación
    path('pasarela/', views.pasarela, name='pasarela'), 
    path('confirmac/<int:orden_id>/', views.confirmacion, name='confirmar'), 
    path('confirmar/', views.confirmar, name='confirmar'),

    # Manual de usuario
    path('manual/', views.manual, name='manual'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
