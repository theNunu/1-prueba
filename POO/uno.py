class Champion:
    def __init__ (self, name, age, role, health):
        self.name = name
        self.age = age
        self.role = role
        self.health = health
        
    def show_information(self):
        return f"Name: {self.name}, Age: {self.age}, Role: {self.role}, tu vida es de: {self.health}"
    
    def hacer_acciones(self, accion):
        acciones = ["curar", "atacar", "defender"]
        if accion in acciones:
            return f"El campeón hace la accion: {accion}."
        else:
            return f"la accion {accion} no existe"
        
        
    def atacar_to_enemy(self):

        import random
        daño = random.randint(0 , self.health)
        resto_vida = self.health - daño
        return f"el campeón {self.name} ataca y recibe un daño de:  {daño}, y le queda {resto_vida} de vida"
        
    
if __name__ == "__main__":
    champion = Champion("Garen", 25, "Fighter", 10)
    print(champion.show_information())
    print(champion.hacer_acciones("atacar"))
    print(champion.atacar_to_enemy())
