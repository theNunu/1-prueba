"""  
El bloque try y except permite al programador manejar errores y excepciones en el código,
evitando que el programa se bloquee en caso de que se produzca un error.

try:
    # Código que podría generar una excepción
except TipoExcepcion:
    # Acciones a realizar en caso de excepción
    
"""


# try:
#     numero = int("abc")
# except ValueError as e:
#     print("Se produjo un ValueError: ", e)
# except TypeError as e:
#     print("Se produjo un TypeError: ", e)
    
try:
    num1 = 1
    num2 = '3'
    
    result = num1 + num2
    
except TypeError as error:
    print("error con el valor de una variable: ", error)
    
    

