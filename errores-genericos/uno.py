try:
    num1 = 1
    num2 = '3'
    result = num1 + num2  # Genera un TypeError
except Exception as error:
    print("Ocurrió un error: ", error)
    print("Tipo de error: ", type(error).__name__)

"""
❯ python errores-genericos/uno.py                                                                                              
Ocurrió un error: unsupported operand type(s) for +: 'int' and 'str'                                                           
Tipo de error: TypeError
"""