print("""  
      
        Convertir Python a JSON (Serialización)
      """)

import json

# Crear un diccionario Python
data = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Convertir el diccionario a una cadena JSON
json_data = json.dumps(data)

print(json_data)