# Importar las bibliotecas NumPy y Matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Generar datos de una distribución normal con media 0 y desviación estándar 1
datos_normal = np.random.normal(0, 1, 10000)

# Generar datos de una distribución normal con media 2 y desviación estándar 0.5
datos_personalizados = np.random.normal(2, 0.5, 10000)

datos_personalizados2 = np.random.normal(2, 1, 10000)

# Crear un histograma para los datos generados
plt.hist(datos_normal, bins=30, density=True, alpha=0.5, color='b', label='Media 0, Desviación 1')
plt.hist(datos_personalizados, bins=30, density=True, alpha=0.5, color='r', label='Media 2, Desviación 0.5')
plt.hist(datos_personalizados2, bins=30, density=True, alpha=0.5, color='c', label='Media 2, Desviación 10')

# Agregar etiquetas y leyendas
plt.xlabel('Valores')
plt.ylabel('Densidad de Probabilidad')
plt.title('Distribución Normal')
plt.legend()

# Mostrar el histograma
plt.show()