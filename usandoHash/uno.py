import hashlib

# Texto de entrada
texto = "Hola mundo"

# Crear un objeto hash usando SHA-256
hash_object = hashlib.sha256()

# Convertir la cadena a bytes (requerido por hashlib)
hash_object.update(texto.encode('utf-8'))

# Obtener el hash en formato hexadecimal
hash_resultado = hash_object.hexdigest()

print(f"Hash de '{texto}': {hash_resultado}")
texto = "Hola"
print(f"Hash de '{texto}': {hash_resultado}")