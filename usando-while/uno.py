x = ["Uno", "Dos", "Tres"]
"""
También podemos usar otro tipo de operación dentro del while, como la que se muestra a continuación.
En este caso tenemos una lista que mientras no este vacía, VAMOS ELIMINANDO SU PRIMER ELEMENTO
"""
while x:
    x.pop(0)
    print(x)
#['Dos', 'Tres']
#['Tres']
#[]

palabras = ['fratello', 'sorella', 'cane', 'libre', 'blood', 'dog']

while palabras:
    palabras.pop(0)
    print(palabras)