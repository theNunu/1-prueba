class Calculadora:
    def __init__(self, valor_inicial):
        self.valor = valor_inicial
    
    def sumar(self, numero1, numero2):
        # numero1 y numero2 no están en __init__, son parámetros locales
        resultado = numero1 + numero2
        self.valor += resultado  # Modificamos un atributo de instancia
        return resultado

# Creamos una instancia
calc = Calculadora(10)
print(calc.sumar(5, 3))  # Salida: 8 (resultado de 5 + 3)
print(calc.valor)        # Salida: 18 (10 + 8)