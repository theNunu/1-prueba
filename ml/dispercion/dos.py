import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     #lista 1
y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]   #lista 2

# Crear el diagrama de dispersión
plt.scatter(x, y)

# Agregar etiquetas a los ejes
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Agregar título al gráfico
plt.title('Diagrama de Dispersión')

# Mostrar el gráfico
plt.show()