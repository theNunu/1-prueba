
print("""   
    En la siguiente función podemos ver como tenemos una variable n que incrementada en 1,
    y después retorna con yield. Lo que pasará aquí, es que el generador generará 
    un total de tres valores.


""")
def generador():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

print('Una cuarta llamada daría un error, ya que no hay más código que ejecutar.')

g = generador()
print(next(g))
print(next(g))
print(next(g))
# Salida: 1, 2, 3
