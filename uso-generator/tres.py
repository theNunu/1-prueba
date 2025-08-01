print('-+-+-+-+- ejemplo con list comprehensions (Comprensión.)-+-+-+-')


lista = [2, 4, 6, 8, 10]
al_cuadrado = [x**2 for x in lista] # SE ELEVA AL CUADRADO  multiplica numero por sí mismo dos veces.
print('imprimir una lista elevaada al cuadrado')
print(al_cuadrado)
# [4, 16, 36, 64, 100]

other_list = [5, 10, 15, 20, 25, 30] #  multiplica numero por sí mismo tres veces.
a_la_quinta = [ n **5 for n in other_list]
print('lista elevada a la quinta: ')
print(a_la_quinta)

nombres = ['alexis', 'kevin', 'britany']
print(nombres)
print('-+'.join(nombres))

for n in other_list:
    print(n ** 5)

try:
    print(', '.join(other_list)) #error porque es un array de numeros
    print('array impreso con exito')
except Exception as error:
    print("Tipo de error:", type(error).__name__)



print("""
    | ------------------------------|
    | MAS EJEMPLOS, SIGUAN VIENDO   |
    |  -----------------------------|
""")

w = "si una función contiene al menos una sentencia yiELd, se convertirá en una función generadora."
wdw = w.upper()
print(wdw)
lista_seis = [6, 36, 1296, 1679616]
al_sexto_generador = (x**6 for x in lista_seis) # elevar el numero itself 6 veces

# Salida: <generator object <genexpr> at 0x103e803b8>
print('lista elevada a la sexta: ')
print(al_sexto_generador)

print('lista elevada a la sexta mediante bucle for: ')
for i in al_sexto_generador:
    print(i ** 6)






