
from uuid import uuid4

id_usuario = uuid4()

usuarios = [
    {
        "id: ": str(uuid4()),
        "nombre": "juanito",
        "apellido": "piguave"    
    },
    {
        "id: ": str(uuid4()),
        "nombre": "walter",
        "apellido": "white"
    },
    {
        "id: ": str(uuid4()),
        "nombre": "jesse",
        "apellido": "pinkman"
    }
    
]

for usuario in usuarios:
    print(f" usuario: {usuario}")
    
    

characater = {
    "nombre": "juanito",
    "apellido": "piguave",
    "edad": 25,
    "altura": 1.75,
    "peso": 70.5,
}


print("imprimiendo el character: ")
for c, v in characater.items():
    print(c, v)
    
