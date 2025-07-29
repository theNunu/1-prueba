class Calculadora:
    def __init__(self, valor_inicial):
        self.valor = valor_inicial
    
    def sumar(self, valor):
        # 'valor' es una variable local, 'self.valor' es un atributo de instancia
        self.valor += valor
        return self.valor

# Creamos una instancia
calc = Calculadora(10)
print(calc.sumar(5))  # Salida: 15
print(calc.valor)     # Salida: 15

""" Dentro del método sumar, hay dos variables llamadas valor:
valor (sin self) es una variable local, pasada como parámetro al método.
self.valor es el atributo de instancia, que persiste en el objeto.
Usar self evita la confusión entre estas dos variables y asegura que estamos modificando el atributo de la instancia.
"""