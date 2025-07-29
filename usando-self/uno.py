class Persona:  # clase
    """      **********    self es una convención    ***********
    self es el nombre que se le da al primer parámetro de los métodos
    de una clase para hacer ***referencia al objeto que está ejecutando ese método.***

    ---------  En Python, self debe ser el primer parámetro en la definición de 
    cualquier método de instancia dentro de una clase.  ------------
    """
    def __init__(self, nombre, edad, trabajo):   # metodo 1
        # Inicializamos atributos de instancia usando self
        self.nombre = nombre
        self.edad = edad
        self.trabajo = trabajo
    
    def presentarse(self):  # metodo 2
        # Accedemos a los atributos de la instancia usando self
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."
    
    def oficio(self):
        return f"trabajo como {self.trabajo} "

# Creamos una instancia de la clase Persona
persona1 = Persona("Ana", 25, "profesora")
print(persona1.presentarse())
print(persona1.oficio())

# Llamamos al método presentarse
print(persona1.presentarse())  # Salida: Hola, soy Ana y tengo 25 años.
persona2 = Persona("alexis", 20, "vacunador")
print(persona2.presentarse())
print(persona2.oficio())

""" 
En el método __init__, self.nombre y self.edad son atributos de instancia.
Esto significa que cada objeto Persona tendrá su propio nombre y edad.
En el método presentarse, usamos self.nombre y self.edad para acceder a los valores de la instancia actual.
Cuando llamamos persona1.presentarse(), Python pasa automáticamente persona1 como el parámetro self.
"""
