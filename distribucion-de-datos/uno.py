# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt

print(""" creeacion de un historograma 
        |**********************| DISTRIBUCION NORMAL  |***********************|
            Histograma
        Un histograma es una representación gráfica de la distribución de datos. 
        Divide el rango de valores de una variable en intervalos y muestra cuántos valores 
        caen en cada intervalo. La función hist() de la biblioteca Matplotlib es una herramienta
        común para crear histogramas en Python.
      """)

# Crear datos de ejemplo (distribución normal)
datos_normal = np.random.normal(0, 1, 1000)

# Crear un histograma para la distribución normal
#El histograma muestra la distribución de los valores en 30 intervalos.
plt.hist(datos_normal, 30, density=True, alpha=0.5, color='c') 
#crea un histograma con 30 intervalos utilizando Matplotlib para visualizar la distribución normal.

# Mostrar el histograma
plt.show()