#   MEDIA    MODA   MEDIANA

import numpy as np
import statistics

data = [10, 20, 30, 40, 50, 10]

# Calcula la media utilizando la función mean() de NumPy
mean = np.mean(data)
print("calcular la media mean(): ")
print("Media:", mean)
# La función np.mean() de NumPy se utiliza para calcular la media aritmética de una lista o array.

data2 = [23, 45, 56, 12, 67, 34, 55, 21]

mean2 = np.mean(data2)

print("otro ejemplo de media", mean2)

print("calcular la moda mode(): ")

# Calcula la moda utilizando la función mode() de statistics
mode = statistics.mode(data)
#statistics.mode() se utiliza para encontrar el valor que aparece con mayor frecuencia en una lista.

print("Moda:", mode)

print("calcular la mediana median(): ")

data3 = [10, 20, 30, 40, 50]

# Calcula la mediana utilizando la función median() de NumPy
median = np.median(data3)

print("Mediana:", median)

"""
 Al calcular la mediana, primero se ordena la lista en orden ascendente: [10, 20, 30, 40, 50] .
 Dado que la lista tiene un número impar de elementos, el valor en la posición central es 30 , 
 que es la mediana.  
"""