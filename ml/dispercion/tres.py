import numpy as np
import matplotlib.pyplot as plt

# Generar 1000 datos aleatorios de una distribución normal con media 5 y desviación estándar 1
x = np.random.normal(5.0, 1.0, 1000)

# Generar 1000 datos aleatorios de una distribución normal con media 10 y desviación estándar 2
y = np.random.normal(10.0, 2.0, 1000)

# Crear un gráfico de dispersión (scatter plot) de los datos generados
plt.scatter(x, y)

# Mostrar el gráfico
plt.show()