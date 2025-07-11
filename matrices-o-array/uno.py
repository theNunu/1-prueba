vinos =[ "Tinto","Blanco", "Rosado"] #array con tres elementos

print(vinos)
vino = [1]
print('obtener el blanco:' , vinos[1])

print("Modificar un Array o Matriz en Python")
print(vinos)
vinos[0] = "jhonny walker"

print(vinos)

print("Longitud de un Array o matriz en Python")
longitud = len(vinos)
print(longitud)  # Salida: 3

print(" -- Recorrer todos los elementos de un Array o una matriz en Python ---")

for vino in vinos:
    print(vino)
    
print("Agregar un elemento a un Array o una matriz")

print(vinos)
vinos.append("red lable")
print( "agregado un vino mas: ", vinos)

print("Eliminar un elemento de un Array o una matriz")

print(vinos)
vinos.remove("Rosado") #vinos.pop(2)
print(vinos)

print("array ordenado")
x = vinos.sort()
print(x)