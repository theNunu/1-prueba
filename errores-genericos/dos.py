try:
    opcion = input("Ingresa una opción (1, 2 o 3): ")

    def caso_1():
        return 10 / 0  # Genera ZeroDivisionError

    def caso_2():
        return int("abc")  # Genera ValueError

    def caso_3():
        lista = [1, 2, 3]
        print(lista[10])  # Genera IndexError

    switch = {
        "1": caso_1,
        "2": caso_2,
        "3": caso_3
    }

    if opcion in switch:
        switch[opcion]()
    else:
        print("error desconocido (no se encuentra dentro de las funcione que usaste)")  # Genera NameError

except Exception as error:
    print("Mensaje del error: ", error)
    print("Tipo de error: ", type(error).__name__)