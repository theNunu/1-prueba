class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = {}  # Diccionario para almacenar libros y cantidades
    
    def agregar_libro(self, titulo, cantidad):
        # Parámetros adicionales no definidos en __init__
        self.libros[titulo] = self.libros.get(titulo, 0) + cantidad
        return f"Agregados {cantidad} ejemplares de '{titulo}' a {self.nombre}"
    
    def prestar_libro(self, titulo, cantidad=1):
        # Método con parámetro opcional
        if titulo in self.libros and self.libros[titulo] >= cantidad:
            self.libros[titulo] -= cantidad
            return self._actualizar_estado(titulo)  # Llamada a otro método
        return f"No hay suficientes ejemplares de '{titulo}'"
    
    def _actualizar_estado(self, titulo):
        # Método interno (convención con guión bajo)
        return f"'{titulo}' ahora tiene {self.libros[titulo]} ejemplares en {self.nombre}"

# Creamos una instancia
biblio = Biblioteca("Biblioteca Central")
print(biblio.agregar_libro("El Quijote", 5))  # Salida: Agregados 5 ejemplares de 'El Quijote' a Biblioteca Central
print(biblio.prestar_libro("El Quijote", 2))  # Salida: 'El Quijote' ahora tiene 3 ejemplares en Biblioteca Central
print(biblio.prestar_libro("El Quijote", 4))  # Salida: No hay suficientes ejemplares de 'El Quijote'