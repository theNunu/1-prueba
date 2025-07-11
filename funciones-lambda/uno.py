#Las funciones lambda en Python son una forma concisa y eficiente de
# definir pequeñas funciones anónimas en una sola línea de código.

"""
nombre_funcion = lambda argumentos: expresion

"""

doble = lambda x: x * 2
print(doble(5))  # Salida: 10

print("Funciones Lambda con Condiciones")
triplicar = lambda x: x * 3 if x > 10 else x
print(triplicar(5))  # Salida: 5
print(triplicar(15)) # Salida: 45

"""
En este caso, hemos creado una función lambda llamada triplicar que toma un argumento x . 
Si x es mayor que 10, la función devuelve el valor de x multiplicado por 3,
lo que triplica el número. Si x es 5 (que es menor que 10), la función simplemente devuelve el
mismo valor. Esto se ilustra con las salidas 5 y 45 respectivamente.
"""

print("Utilizando Funciones Lambda en Funciones Integradas")

numeros = [1, 2, 3, 4, 5] #lista de numeros
cuadrados = map(lambda x: x ** 2, numeros)
print(list(cuadrados))  # Salida: [1, 4, 9, 16, 25] convertimos el resultado en una lista con list()
print(cuadrados)

"""
En este ejemplo, hemos definido una lista de números y luego usamos la función map()
junto con una función lambda para calcular los cuadrados de los números en la lista. 
La función map() aplica la función lambda a cada elemento de la lista numeros , y 
convertimos el resultado en una lista con list() . Como resultado, obtenemos una
lista de los cuadrados de los números en [1, 4, 9, 16, 25] .

"""