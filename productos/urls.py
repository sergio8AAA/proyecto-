from django.urls import path
from . import views

urlpatterns = [
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
]
