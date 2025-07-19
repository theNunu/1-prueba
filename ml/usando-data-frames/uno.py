import pandas as pd
print(" --------   USADO PARA EL ANALISIS/ MANEJO DE DATOS CATEGORICOS   -------")
data = {
    'Nombre': ['Juan', 'Maria', 'Pedro', 'Ana', 'Luis'],
    'Edad': [25, 30, 28, 22, 27],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Madrid', 'Valencia']
}

df = pd.DataFrame(data)

print(df)