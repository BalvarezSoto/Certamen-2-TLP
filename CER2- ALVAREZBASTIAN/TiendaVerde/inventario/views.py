from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Producto, Pedido
from .forms import CustomCreationForm
from .Carrito import Carrito
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import Group

# Create your views here.
def index(request):
    return render(request, 'core/Index.html')

@login_required
def Catalogo(request):
    productos = Producto.objects.all()
    data={
        'productos': productos
    }
    return render(request, 'core/Catalogo.html', data)

def exit(request):
    logout(request)
    return redirect('/')

def registro(request):
    data = {
        'form': CustomCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            clientes_group = Group.objects.get(name='Clientes')
            user.groups.add(clientes_group)
            login(request, user)
            return redirect(to="index")
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)

@login_required
def tienda(request):

    productos = Producto.objects.all()
    return render(request, "core/Carro.html", {'productos':productos})

def agregar_productos(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('Catalogo')

def eliminar_producto(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('Catalogo')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('Catalogo')

def limpiar(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('Catalogo')

def Confirmar(request):
    if request.user.is_authenticated:
        carrito = Carrito(request)
        if carrito.carrito: 
            pedido = Pedido.objects.create(
                cliente=request.user,
                total=sum(item["acumulado"] for item in carrito.carrito.values()), 
                estado='pendiente'
            )
            for key, item in carrito.carrito.items():
                producto = Producto.objects.get(id=item["producto_id"])
                pedido.productos.add(producto)
            pedido.save()
            carrito.limpiar()
            return redirect('Catalogo')
    return redirect('Catalogo')

def es_vendedor(user):
    return user.groups.filter(name='Vendedores').exists()

@login_required
@user_passes_test(es_vendedor)
def listar_pedidos(request):
    if request.method == 'POST':
        pedido_id = request.POST.get('pedido_id')
        nuevo_estado = request.POST.get('estado')
        pedido = Pedido.objects.get(id=pedido_id)
        pedido.estado = nuevo_estado
        pedido.save()
        return redirect('ListarPedidos')
    pedidos = Pedido.objects.all() 
    return render(request, 'core/Pedidos.html', {'pedidos': pedidos})