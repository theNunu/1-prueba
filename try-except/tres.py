try:
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    result = num1 / num2
    print("Resultado:", result)
except ValueError as ve:
    print("Error: Ingresa solo números válidos: ", ve)
except ZeroDivisionError as zde:
    print("Error: No se puede dividir por cero: ", zde)
except Exception as error:
    print("Error inesperado: ", error)
    
""" 
1. ValueError: Si el usuario ingresa algo que no se puede convertir a int (como 'abc').

2. ZeroDivisionError: Si el usuario ingresa 0 como divisor.

3. Exception: Captura cualquier otro error no previsto (por ejemplo, un error 
de memoria o una interrupción del programa).
    
    Usa except Exception como respaldo: Si quieres una red de seguridad para errores
    inesperados, colócala después de las excepciones específicas.
"""