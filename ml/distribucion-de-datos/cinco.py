# Importar la biblioteca SciPy
import scipy.stats as stats

# Definir la media y la desviación estándar
media = 3
desviacion = 1

# Calcular la probabilidad de que x esté entre 2 y 4
probabilidad = stats.norm.cdf(4, loc=media, scale=desviacion) - stats.norm.cdf(2, loc=media, scale=desviacion)

print("La probabilidad de que x esté entre 2 y 4 es:", probabilidad)