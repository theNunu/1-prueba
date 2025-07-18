from scipy import stats
import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
y = [50, 42, 38, 30, 28, 24, 22, 20, 18, 16]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

speed = myfunc(10)


plt.title('otro ejemplo')
plt.scatter(x, y)
plt.grid(True) # para que aparezca cuadros en el grafico
plt.show()
print(speed)