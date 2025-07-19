print("""
      SALIDA DE FECHA:
      
      . Algunos ejemplos de códigos de formato comunes son:

    %Y : Año con siglo como un número decimal de cuatro dígitos.
    %m : Mes como número decimal (01, 02, …, 12).
    %d : Día del mes como número decimal (01, 02, …, 31).   
    %H : Hora (00, 01, …, 23).
    %M : Minuto (00, 01, …, 59).    
    %S : Segundo (00, 01, …, 59).
            
      """)

import datetime
fecha_actual = datetime.date(2025, 8, 9)
print(fecha_actual)  # Salida: 2023-08-03

print("El Método strftime()")
fecha_actual = datetime.date(2023, 8, 3)
cadena_fecha = fecha_actual.strftime("%Y-%m-%d")
print(cadena_fecha)  # Salida: 2023-08-03

print("otro ejemplo")

date_now = datetime.datetime.now()
date = date_now.strftime("dia de hoy: %A,mes de hoy: %B %Y-%m-%d %H:%M:%S:%f")

print(f"Fecha y hora actual: {date}")  # Salida: Fecha y hora actual: 2023-08-03 12:34:56 (ejemplo)