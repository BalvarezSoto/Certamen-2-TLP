from django.urls import path
from inventario.views import index, Catalogo, exit, registro, tienda,\
                             agregar_productos, eliminar_producto, restar_producto, limpiar,\
                             Confirmar,listar_pedidos
urlpatterns = [
    path('', index, name = 'index'),
    path('Catalogo/', Catalogo, name = 'Catalogo'),
    path('logout/', exit, name='exit'),
    path('registro/', registro, name = 'registro'),
    path('Carro/', tienda, name = 'Carro'),
    path('agregar/<int:producto_id>/', agregar_productos, name="Añadir"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Eliminar"),
    path('restar/<int:producto_id>/', restar_producto, name="Restar"),
    path('limpiar/', limpiar, name="Limpiar"),
    path('confirmacion/', Confirmar, name="confirmar"),
    path('pedidos/', listar_pedidos, name='ListarPedidos'),
]