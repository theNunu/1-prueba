try:
    archivo = open("no_existe.txt", "r")  # Esto genera un FileNotFoundError
    contenido = archivo.read()
    archivo.close()
except Exception as error:
    print("Ocurrió un error al trabajar con el archivo:", error)
    print("Tipo de error:", type(error).__name__)