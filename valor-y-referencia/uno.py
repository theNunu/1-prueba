
print("""  
    -------------------------------------------------------------------------------------
     |   el comportamiento estará definido por el tipo de variable con la que estamos tratando. 
     |   Veamos un ejemplo de paso por valor.
    ---------------------------------------------------------------------------------------

""")
x = [10, 20, 30, 40]
def funcion(x):
    x.append(50)
funcion(x)



entrada = 10
def funcion(entrada):
    entrada = 0
funcion(entrada)

print(x) # 10

print("""  
    Una forma muy útil de saber lo que pasa por debajo de Python, es haciendo uso de la función id().
    Esta función nos devuelve un identificador único para cada objeto. Volviendo al primer ejemplo podemos 
    ver como los objetos a los que “apuntan” x y entrada son distintos.
""")

x = 10
print(id(x)) # 4349704528
def funcion(entrada):
    entrada = 0
    print(id(entrada)) # 4349704208

funcion(x)