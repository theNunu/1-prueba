import numpy as np

"""  
Percentiles con NumPy
    El módulo NumPy tiene un método para encontrar el percentil especificado. 
    Use el método NumPy percentile() para encontrar los percentiles:
"""

data = [23, 45, 56, 12, 67, 34, 55, 21]

# Calcular el percentil 25
percentile_25 = np.percentile(data, 25)

# Calcular el percentil 50 (mediana)
percentile_50 = np.percentile(data, 50)

# Calcular el percentil 75
percentile_75 = np.percentile(data, 75)

print("Percentil 25:", percentile_25)
print("Percentil 50 (Mediana):", percentile_50)
print("Percentil 75:", percentile_75)

print("""
      -------   Percentiles con Panda --------
      """)

import pandas as pd

data = [23, 45, 56, 12, 67, 34, 55, 21]

# Crear un DataFrame con los datos
df = pd.DataFrame(data, columns=['valor'])

# Calcular el percentil 25
percentile_25 = df['valor'].quantile(0.25)

# Calcular el percentil 50 (mediana)
percentile_50 = df['valor'].quantile(0.50)

# Calcular el percentil 75
percentile_75 = df['valor'].quantile(0.75)

print("Percentil 25:", percentile_25)
print("Percentil 50 (Mediana):", percentile_50)
print("Percentil 75:", percentile_75)