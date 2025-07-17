# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt

print("""
      
      DISTRIBUCION UNIFORME
      """)
# Crear datos de ejemplo (distribución uniforme)
datos_uniforme = np.random.uniform(0, 1, 1000)

# Crear un histograma para la distribución uniforme
plt.hist(datos_uniforme, 30, density=True, alpha=0.5, color='g')

# Mostrar el histograma
plt.show()