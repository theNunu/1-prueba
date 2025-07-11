
import asyncio
#La función sleep puede suspender la ejecución de una rutina durante algún tiempo.
async def fun_a(t):
    for i in range(t):
        print("fun_a", end=" ")
        await asyncio.sleep(1)
    return 1


async def fun_b(t):
    for i in range(t): #range => gama
        print("fun_b", end=" ")
        await asyncio.sleep(1)
    return 2

async def main():
    results = await asyncio.gather(fun_a(2), fun_b(3)) #gather => reunir
    print(results) #SE REPITE un numero de VECES

my_loop = asyncio.get_event_loop()
my_loop.run_until_complete(main())
# [1, 2] es la tupla que recibe la función main de nuestras funciones asíncrona