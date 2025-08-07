def contar_palabras(frase):
    """
    Toma una frase y devuelve un diccionario con el conteo de cada palabra.
    """
    # 1. Convertir la frase a minúsculas y dividirla en una lista de palabras.
    #    .lower() asegura que 'Hola' y 'hola' se cuenten como la misma palabra.
    #    .split() divide la frase por espacios en blanco.
    palabras = frase.lower().split()
    
    # 2. Crear un diccionario vacío para almacenar el conteo de palabras.
    conteo_palabras = {}

    # 3. Recorrer la lista de palabras para contarlas.
    for palabra in palabras:
        # Si la palabra ya está en el diccionario, incrementa su conteo.
        if palabra in conteo_palabras:
            conteo_palabras[palabra] += 1
        else:
            # Si la palabra no está, la añade al diccionario con un conteo de 1.
            conteo_palabras[palabra] = 1

    return conteo_palabras

# --- Lógica principal del programa ---
# 1. Pedirle al usuario que ingrese una frase.
frase_ingresada = input("Ingresa una frase para contar sus palabras: ")

# 2. Llamar a la función y guardar el diccionario que devuelve.
resultado = contar_palabras(frase_ingresada)

# 3. Imprimir el resultado final.
print("\nConteo de palabras:")
print(resultado)

# Ejemplo de cómo se vería la salida si ingresas: "Hola hola mundo, Hola de nuevo"
# Conteo de palabras:
# {'hola': 3, 'mundo,': 1, 'de': 1, 'nuevo': 1}