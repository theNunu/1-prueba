try:
    num = int(input("Ingresa un número: "))
    result = 10 / num
    print("Resultado:", result)
except Exception as error:
    print("Ocurrió un error:", error)