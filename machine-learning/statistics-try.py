import statistics as stats

# Datos de ejemplo
datos = [4, 5, 8, 7, 6, 9, 5, 7]

# Calcular la desviación estándar utilizando la biblioteca statistics
desviacion_estandar = stats.stdev(datos)

print("Desviación Estándar:", desviacion_estandar)


print(" --  -- mas desviacion estandar: ")

velocidad = [99, 86, 87, 88, 86, 87, 85]
des_stand = stats.stdev(velocidad)
print(des_stand)

velocidad2 = [32, 111, 138, 28, 59, 77, 97]
print("Desviación Estándar de velocidad2:", stats.stdev(velocidad2))