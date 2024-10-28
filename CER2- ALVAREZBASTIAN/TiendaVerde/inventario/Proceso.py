def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carro" in request.session.keys():
            for key, value in request.session["carro"].items():
                acumulado = value.get("acumulado", 0)
                total += int(acumulado)
    return {"total_carrito": total}

def grupos_usuario(request):
    if request.user.is_authenticated:
        grupos = request.user.groups.values_list('name', flat=True)
        return {'grupos_usuario': grupos}
    return {'grupos_usuario': []}