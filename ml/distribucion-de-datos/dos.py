print(""" 
      ====== grandes conjuntos de datos ======
      
    Histograma
        Un histograma es una representación gráfica de la distribución de datos. 
        Divide el rango de valores de una variable en intervalos y muestra cuántos valores 
        caen en cada intervalo. La función hist() de la biblioteca Matplotlib es una herramienta
        común para crear histogramas en Python.
      """)

# Importar la biblioteca Pandas
import pandas as pd

# URL del archivo CSV de ejemplo (puedes reemplazarlo con la URL de tu propio conjunto de datos)
url = 'https://ejemplo.com/conjunto_de_datos_grande.csv'

# Cargar el conjunto de datos desde la URL en un DataFrame de Pandas
df = pd.read_csv(url)

# Mostrar las primeras filas del DataFrame para verificar
print(df.head())