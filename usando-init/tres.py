class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = {}
    
    def agregar_producto(self, producto, cantidad):
        # Parámetros producto y cantidad no están en __init__
        self.inventario[producto] = cantidad
        return f"Agregado {cantidad} de {producto} a {self.nombre}"
    
    def vender(self, producto, cantidad):
        # Llamamos a otro método con parámetros
        if producto in self.inventario and self.inventario[producto] >= cantidad:
            return self.actualizar_inventario(producto, cantidad)
        return "No hay suficiente inventario."
    
    def actualizar_inventario(self, producto, cantidad):
        self.inventario[producto] -= cantidad
        return f"Vendidos {cantidad} de {producto}. Inventario restante: {self.inventario[producto]}"

# Creamos una instancia
tienda = Tienda("Supermercado XYZ")
print(tienda.agregar_producto("Manzanas", 50))  # Salida: Agregado 50 de Manzanas a Supermercado XYZ
print(tienda.vender("Manzanas", 10))          # Salida: Vendidos 10 de Manzanas. Inventario restante: 40