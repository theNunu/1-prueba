# Importar las bibliotecas necesarias
import matplotlib.pyplot as plt
from scipy import stats
"""  
    1. Importamos la biblioteca Matplotlib para trazar gráficos y la biblioteca SciPy para realizar análisis estadísticos.
    2. Creamos dos listas x e y que representan la edad y la velocidad de los automóviles.
    3. Calculamos la pendiente, la intercepción, el coeficiente de correlación r , el valor p y el error estándar utilizando stats.linregress .
    4. Definimos una función myfunc que utiliza la pendiente e intercepción para calcular la velocidad prevista.
    5. Creamos un nuevo conjunto de datos mymodel aplicando la función myfunc a cada valor de x .
    6. Dibujamos el diagrama de dispersión original y la línea de regresión lineal.
"""

# Datos de ejemplo
x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
y = [50, 42, 38, 30, 28, 24, 22, 20, 18, 16]

# Realizar la regresión lineal
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Definir una función lineal
def myfunc(x):
  return slope * x + intercept

# Calcular los valores ajustados
mymodel = list(map(myfunc, x))

# Crear un gráfico de dispersión y la línea de regresión
plt.scatter(x, y)
plt.plot(x, mymodel)

plt.xlabel("eje x")
plt.ylabel("eje y")
plt.title("la regresion lineal")
plt.show()