class ErrorEjemplo:

    def __init__(self, dato):
        # Sin self, 'dato' es solo una variable local
        self.dato = dato

    """      **********    self es una convención    ***********
    ++++++   para inicializar atributos de instancia como para acceder y manipular métodos y atributos de instancia ++++++
    self es el nombre que se le da al primer parámetro de los métodos
    de una clase para hacer ***referencia al objeto que está ejecutando ese método.***

    ---------  En Python, self debe ser el primer parámetro en la definición de 
    cualquier método de instancia dentro de una clase.  ------------
    # Llamamos a otros métodos usando self
    """
    
    def obtener_dato(self):
        # Esto causará un error porque 'dato' no existe como atributo
        return self.dato

# Creamos una instancia
obj = ErrorEjemplo("test")
try:
    print(obj.obtener_dato())
except AttributeError as e:
    print(f"Error: {e}")  # Salida: Error: 'ErrorEjemplo' object has no attribute 'dato'
    print("Tipo de error:", type(e).__name__)