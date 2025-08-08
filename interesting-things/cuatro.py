
import os

from pathlib import Path


gavilan = 'interesting-things/archivos_txt/gavilan.txt'
stats = os.stat(gavilan)

tamanio = stats.st_size  # Tamaño en bytes
print(f"Tamaño: {tamanio} bytes")

tamanio = stats.st_size  # Tamaño en bytes
