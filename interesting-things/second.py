import os
from datetime import datetime

# Ruta al archivo
archivo = "interesting-things/prueba.txt"

# Obtener metadatos
stats = os.stat(archivo)
# print('el metadato es: ' , stats)
# Extraer información
tamanio = stats.st_size  # Tamaño en bytes
fecha_creacion = datetime.fromtimestamp(stats.st_ctime)  # Fecha de creación
fecha_modificacion = datetime.fromtimestamp(stats.st_mtime)  # Fecha de última modificación

# Mostrar metadatos
print(f"Metadatos del archivo {archivo}:")
print(f"Tamaño: {tamanio} bytes")
print(f"Fecha de creación: {fecha_creacion}")
print(f"Fecha de última modificación: {fecha_modificacion}")