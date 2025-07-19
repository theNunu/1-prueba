# Importar la biblioteca SciPy
from scipy import stats

x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
y = [50, 42, 38, 30, 28, 24, 22, 20, 18, 16]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)
