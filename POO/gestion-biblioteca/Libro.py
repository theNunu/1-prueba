import uuid
id_libri = uuid.uuid4()

class Libro:
    def __init__(self, nombre, autor, disponible = True, id_libro = id_libri):
        self.id_libro = id_libro
        self.nombre = nombre
        self.autor = autor
        self.disponible = disponible

    def mostrar_info(self):
        return f""" 
            id: {self.id_libro}
            nombre: {self.nombre}
            autor: {self.autor}
            disponible: {self.disponible}
        """
    def prestar_libro(self):
        if self.disponible:
            respuesta = print(f"El libro {self.nombre} ha sido prestado. NO LO PUEDES PRESTAR")
        else:
            respuesta =print(f"El libro {self.nombre} ha sido prestado")

        return respuesta

    




libro = Libro("el libro troll", "rubius", False )

print(libro.mostrar_info())

print(libro.prestar_libro())