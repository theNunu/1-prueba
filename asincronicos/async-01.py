
import asyncio
#La función sleep puede suspender la ejecución de una rutina durante algún tiempo.

async def fun_a(repetir): #Parámetro t: Es un entero que determina cuántas veces se ejecutará el bucle for.
    for i in range(repetir):
        print("fun_a", end=" ") #Imprime "fun_a" seguido de un espacio (sin salto de línea, debido a end=" ").
        await asyncio.sleep(1) #Pausa la ejecución de fun_a durante 1 segundo 
        #Durante esta pausa, el bucle de eventos puede ejecutar otras corutinas (como fun_b).
    return 1

async def fun_b(repetir):
    for i in range(repetir): #range => gama
        print("fun_b", end=" ") #Imprime "fun_b" seguido de un espacio (sin salto de línea, debido a end=" ").
        await asyncio.sleep(1)
    return 2

async def main():
    results = await asyncio.gather(fun_a(2), fun_b(3)) #gather => reunir
    #await: Indica que main debe esperar a que gather complete la ejecución de ambas corutinas antes de continuar.
    print(results) #SE REPITE un numero de VECES

my_loop = asyncio.get_event_loop()
my_loop.run_until_complete(main())
# [1, 2] es la tupla que recibe la función main de nuestras funciones asíncrona