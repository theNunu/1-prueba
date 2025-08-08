
import os

from pathlib import Path

# Definir la carpeta base
CANCIONES = Path("interesting-things") / "archivos_txt"

# Definir las rutas de los archivos específicos
GAVILAN = CANCIONES / "gavilan.txt"
TORMENTA = CANCIONES / "tormenta.txt"
TIEMPO = CANCIONES / "vamos_a_darnos.txt"

# Lista de archivos específicos
canciones_jose_jose = [GAVILAN, TORMENTA, TIEMPO]

# Imprimir las rutas de los archivos
print("Rutas de las canciones:")
for cancion in canciones_jose_jose:
    print(cancion)

# Leer el contenido de cada archivo
print("\nContenido de las canciones:")
for cancion in canciones_jose_jose:
    if cancion.exists():  # Verificar que el archivo existe
        with open(cancion, "r", encoding="utf-8") as file:
            contenido = file.read()
            print(f"\nArchivo: {cancion.name}")
            print(contenido)
            
            # Obtener metadatos
            stats = os.stat(cancion)
            tamanio = stats.st_size  # Tamaño en bytes
            print(f"Tamaño: {tamanio} bytes")
            
    else:
        print(f"\nArchivo {cancion.name} no encontrado.")

# Opción adicional: Listar todos los archivos .txt en la carpeta
print("\nTodos los archivos .txt en la carpeta:")
for archivo in CANCIONES.glob("*.txt"):  # Buscar todos los archivos .txt
    print(archivo)