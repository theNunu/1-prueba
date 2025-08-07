print('adivina la letra que falta: ')
print(""" 

P U _ A



""")
respuesta = 'M'


def verificar(respuesta, palabra):
    palabra = palabra.upper()
    if palabra == respuesta:
        print(f'la respuesta es correcta, la palabra secreta era la: {palabra}')
        return True
    else:
        print('respuesta incorrecta')
        return False

validacion = False

while True:
    if not validacion:
        palabra= input('di cual: ')
        validacion = verificar(respuesta, palabra)
        
        # Si validacion es True, la respuesta fue correcta y salimos del ciclo
        if validacion: #if validacion == True
            break

