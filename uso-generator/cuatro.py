print(""" 
los valores no están almacenados en memoria, sino que se van generando al vuelo. 
    Esta es una de las principales ventajas de los generadores, ya que los elementos sólo son generados cuando se piden, 
    lo que hace que sean mucho más eficientes en lo relativo a la memoria.
""")

"""
Llegados a este punto tal vez te preguntes para qué sirven los generadores. 
Lo cierto es que aunque no existieran, podría realizarse lo mismo creando una clase que implemente los métodos __iter__() y __next__(). 
un ejemplo de una clase que genera los primeros 10 números (0,9) al cuadrado.  
"""

class AlCuadrado:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > 9:
            raise StopIteration

        result = self.i ** 2
        self.i += 1
        return result
"""
Y de la misma forma que usábamos los generadores, podemos usar nuestra clase AlCuadrado.
 Creamos un objeto de ella, y la iteramos. En cada iteración generará un nuevo valor nuevo 
 hasta que se llegue al final.  

"""

eleva_al_cuadrado = AlCuadrado()
for i in eleva_al_cuadrado:
    print(i)
#0,1,4,9,16,25,36,49,64,81

