import hashlib

# Textos a hashear
texto1 = "Hola mundo"
texto2 = "Hola Mundo"  # Cambia una mayúscula

# Generar hash SHA-256
hash1 = hashlib.sha256(texto1.encode()).hexdigest()
hash2 = hashlib.sha256(texto2.encode()).hexdigest()

# Mostrar resultados
print(f"Texto 1: {texto1}")
print(f"Hash 1: {hash1}")
print(f"Texto 2: {texto2}")
print(f"Hash 2: {hash2}")
print(f"¿Son iguales los hashes? {hash1 == hash2}")