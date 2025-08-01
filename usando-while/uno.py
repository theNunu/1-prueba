x = ["Uno", "Dos", "Tres"]
"""
También podemos usar otro tipo de operación dentro del while, como la que se muestra a continuación.
En este caso tenemos una lista que mientras no este vacía, VAMOS ELIMINANDO SU PRIMER ELEMENTO
"""
while x:
    x.pop(0)
    print(x)  # el array queda vacio
#['Dos', 'Tres']
#['Tres']
#[]

palabras = ['fratello', 'sorella', 'cane', 'libre', 'blood', 'dog']

while palabras:
    palabras.pop(0)
    print(palabras) # el array queda vacio


print(""" 
    En realidad, se pueden pasar hasta tres parámetros separados por coma, donde el primer es el inicio de la secuencia, 
    el segundo el final y el tercero el salto que se desea entre números. Por defecto se empieza en 0 y el salto es de 1.
    #range(inicio, fin, salto)

""")




print(list(range(5, 20, 2)))

print('usando for:')
""" Por lo tanto, si llamamos a range() con (5,20,2), se generarán números de 5 a  20 (-1) de dos en dos. 
    Un truco es que el range() se puede convertir en list. """
for i in range(5, 20, 2): #from 25 to 19
    print(i) #5,7,9,11,13,15,17,19

print(' ****  otro ejemplo:')    
for i in range (5, 0, -1): #from  5 to 1
    print(i) #5,4,3,2,1


palabras = ['fratello', 'sorella', 'cane', 'libre', 'blood', 'dog']

print(" *** IMPRIMIENDO LA LISTA DE PALABRAS ****")
for logos in palabras:
    print (logos)


print(palabras)
palabras.append('parce')
print(palabras)

print(' --- adding a new list in the list ---')
words_english = ['friend', 'boy', 'can', 'back']
palabras.append(words_english)
print(palabras)
