class Champion:
    def __init__ (self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
        self.health = 100
        
    def show_information(self):
        return f"Name: {self.name}, Age: {self.age}, Role: {self.role}, tu vida es de: {self.health}"
    
    
    def hacer_acciones(self, accion):
        acciones = ["curar", "atacar", "defender"]
        if accion in acciones:
            return f"El campeón hace la accion: {accion}."
        else:
            return f"la accion {accion} no existe"
        
        
    def atacar_to_enemy(self):
        self.vida = 100
        import random
        daño = random.raint(0 , self.vida)
        resto_vida = self.vida - daño
        return f"el campeón {self.name} ataca y recibe un daño de:  {daño}, y le queda {resto_vida} de vida"
        
        
        
        pass
        
        
        
        
    
    
if __name__ == "__main__":
    champion = Champion("Garen", 25, "Fighter")
    print(champion.show_information())
    print(champion.hacer_acciones("atacar"))
    print(champion.atacar_to_enemy())
