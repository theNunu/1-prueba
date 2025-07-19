import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5, 6]     #lista 1
y = [5, 7, 8, 12, 9, 11]   #lista 2

# Crear el diagrama de dispersión
plt.scatter(x, y)

# Agregar etiquetas a los ejes
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Agregar título al gráfico
plt.title('Diagrama de Dispersión')

# Mostrar el gráfico
plt.show()