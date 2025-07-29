class Estudiante:
    # ***************           __init__ es un método especial (o "método mágico") ****************
    """
    __init__ no crea el objeto, sino que lo configura asignando valores a sus atributos. 
    """
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
    
    def mostrar_info(self):
        return f"Estudiante: {self.nombre}, Matrícula: {self.matricula}"

# Creamos una instancia
estudiante = Estudiante("Carlos", "12345")
print(estudiante.mostrar_info())  # Salida: Estudiante: Carlos, Matrícula: 12345