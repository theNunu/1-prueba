import time
import sys

# def download_senior(total=20):
#     print('descargando arhcivo: ')
#     for i in range(total + 1):
#         percent = (i / total) * 100
#         bar = "|" * i + "-" * (total - i)
#         sys.stdout.write(f"\r[{bar}]
#         {percent:5.1f}%")
#         sys.stdout.flush()
#         time.sleep(0.1)       
#     print('\n descarga completada')
    
def download_senior(total=20):
    print('Descargando archivo:')
    for i in range(total + 1):
        percent = (i / total) * 100
        bar = "█ " * i + " " * (total - i)  # Usamos un carácter más visual para la barra
        sys.stdout.write(f"\r[{bar}] {percent:5.1f}%")  # \r para sobrescribir la línea
        sys.stdout.flush()
        time.sleep(0.1)
    print('\nDescarga completada')    
    
download_senior()