print("""   
    |--------------------------------------- |
                Generators en Python                        
    |--------------------------------------- |
    si una función contiene al menos una sentencia yield, se convertirá en una función generadora.

""")

def funcion():
    return 5

def generator():
    yield 5

#Y ahora vamos a intentar llamar a las dos “funciones”.

print(funcion())
print(generator()) #se devuelve es en realidad un objeto de la clase generator
# Salida: 5
# Salida: <generator object generador at 0x103e7f0a0>

a = generator()
print(next(a)) # Salida: 5

print(""" 
    Otra de las características que hacen a los generators diferentes, es que pueden ser iterados,
    ya que codifican los métodos __iter__() y __next__(), por lo que podemos usar next() sobre ellos. 
    Dado que son iterables, lanzan también un StopIteration cuando se ha llegado al final.
""")
def generator2():
    yield 10
print(generator2())

generator2 = generator2()
print(next(generator2)) # imprimira 10
print(next(generator2)) #saldra error si se llama 2 VECES Salida: Error! StopIteration:




