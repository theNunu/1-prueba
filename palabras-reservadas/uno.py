frase = "Hola mundo, esto es una prueba"
palabras_divididas = frase.split()

print(palabras_divididas)
# Salida: ['Hola', 'mundo,', 'esto', 'es', 'una', 'prueba']

 #split() toma la frase y la convierte en una lista, donde cada palabra es un elemento. 

print("""

    USO DEL SET()

    Un set es un tipo de colección en Python que tiene una característica muy importante: 
    solo puede contener elementos únicos. Cuando conviertes una lista a un set, todos los elementos 
    duplicados se eliminan automáticamente.

Esto es extremadamente útil para obtener una lista de valores únicos de manera rápida y eficiente.


""")

mi_lista = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(mi_lista)
# Convertir la lista en un set
mi_set = set(mi_lista)

print(mi_set)
# Salida: {1, 2, 3, 4, 5}
# Convertir el set de nuevo a una lista
lista_unica = list(mi_set)

print(lista_unica)
# Salida: [1, 2, 3, 4, 5]