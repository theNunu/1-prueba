class Coche:


    """ Esto muestra cómo self permite acceder tanto a atributos (self.encendido) como a otros métodos de la misma clase """
    def __init__(self, marca, modelo):  # metodo 1
        # Inicializamos atributos de instancia usando self
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
    
    def encender(self):      # metodo 2
        self.encendido = True
        return f"El coche {self.marca} {self.modelo} está encendido."
    
    def apagar(self):            # metodo 3
        self.encendido = False
        return f"El coche {self.marca} {self.modelo} está apagado."
    
    def estado(self):      # metodo 4
        # Llamamos a otros métodos usando self
        if self.encendido:
            return self.encender()
        else:
            return self.apagar()

# Creamos una instancia
coche1 = Coche("Toyota", "Corolla")
print(coche1.estado())  # Salida: El coche Toyota Corolla está apagado.
print(coche1.encender())
print(coche1.estado())  # Salida: El coche Toyota Corolla está encendido.
