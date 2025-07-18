# Importar la biblioteca Matplotlib
import matplotlib.pyplot as plt

# Datos para el diagrama de dispersión
x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
y = [50, 42, 38, 30, 28, 24, 22, 20, 18, 16]

# Crear el diagrama de dispersión
plt.scatter(x, y) # Crear un gráfico de dispersión (scatter plot) de los datos generados

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Diagrama de Dispersión")
plt.grid(True) # para que aparezca cuadros en el grafico
plt.show()