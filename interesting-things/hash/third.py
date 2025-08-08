import os
import hashlib
from datetime import datetime

# Ruta al archivo
archivo = "interesting-things/prueba.txt"

# Leer el contenido del archivo para calcular el hash
with open(archivo, "rb") as f:
    contenido = f.read()
    hash_archivo = hashlib.sha256(contenido).hexdigest()

# Obtener metadatos
stats = os.stat(archivo)
metadatos = {
    "nombre": archivo,
    "tamanio_bytes": stats.st_size,
    "fecha_modificacion": datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
    "hash": hash_archivo
}

# Mostrar metadatos
print("Metadatos del archivo:")
for clave, valor in metadatos.items():
    print(f"{clave}: {valor}")