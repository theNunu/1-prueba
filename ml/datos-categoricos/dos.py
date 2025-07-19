print(""" 
      DATOS CATEGORICOS
      
      Usando listas o tuplas
      """)

print(" ------      Usando listas o tuplas    -------")

try:
    frutas = ['manzana', 'plátano', 'naranja', 'manzana', 'plátano', 'pera']
    colores = ('rojo', 'amarillo', 'naranja', 'verde', 'amarillo', 'verde')
    
    print(frutas[4])
    print(coloress[2])
    
    print("se encontro el index frutas y colores")
    
except Exception as e:
    print(f"hubo un error: {e}")
    print(f"tipo de error: {type(e)}")


print(" ------      Usando diccionarios    -------")

alumnos = {
    'Juan': 'Aprobado',
    'María': 'Reprobado',
    'Pedro': 'Aprobado',
    'Ana': 'Aprobado',
    'Luis': 'Reprobado'
}

""" 
En este ejemplo, el diccionario alumnos representa datos categóricos que indican si un alumno ha sido aprobado o reprobado.
"""

print(alumnos)