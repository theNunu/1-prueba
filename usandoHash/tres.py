class Carril:
    def __init__(self, nombre):
        self.nombre = nombre
        self.campeones = []  # Lista para almacenar los nombres de los campeones
    
    def add_champion(self, campeones):
        # Agrega campeones a la lista, evitando duplicados
        for campeon in campeones:
            if campeon not in self.campeones:
                self.campeones.append(campeon)
        
        #cadena formateada (f-string)
        return f"""
            Nombre del carril: {self.nombre}
            (con .join) Se agregaron los campeones: {', '.join(self.campeones)}
            (sin .join) Se agregaron los campeones: {self.campeones}
            Campeones actuales: {', '.join(self.campeones)}
        """

# Creamos una instancia
carril = Carril("Varón")

# Agregamos campeones
print(carril.add_champion(['Teemo', 'Warwick', 'Fiora', 'Nasus']))

# Agregamos más campeones
print(carril.add_champion(['Garen', 'Teemo']))  # Teemo ya existe, no se duplicará
