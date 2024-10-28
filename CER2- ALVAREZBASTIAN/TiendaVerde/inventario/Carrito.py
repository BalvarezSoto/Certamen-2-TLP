class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carro")
        if not carrito:
            self.session["carro"] = {}
            self.carrito = self.session["carro"]
        else:
            self.carrito = carrito
    
    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad":1,   

            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carro"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1    
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] >= 0:
                if self.carrito[id]["cantidad"] <= 0:
                    del self.carrito[id]
                self.guardar_carrito()

    def limpiar(self):
        self.session["carro"] = {}
        self.carrito = self.session["carro"]
        self.session.modified = True
