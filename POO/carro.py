class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        self.encendido = False

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            return f"Motor de {self.tipo} arrancado."
        return "El motor ya está encendido."

class Coche:
    def __init__(self, marca, modelo, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        # Aquí la clase Coche crea una instancia de la clase Motor (composición)
        self.motor = Motor(tipo_motor)

    def encender_coche(self):
        # La clase Coche llama a un método de la clase Motor
        mensaje = self.motor.arrancar()
        print(f"{self.marca} {self.modelo}: {mensaje}")

# --- Uso ---
mi_coche = Coche("Ford", "Focus", "gasolina")
mi_coche.encender_coche()  # Salida: Ford Focus: Motor de gasolina arrancado.