# word = 'hola'

# word = word.upper()
# print(word)

print("""     
    DAME DOS STRING
""")

def validar(listas_palabras):
    

    son_strings = [isinstance(p, str) for p in listas_palabras]
    # Si 'all()' devuelve True, significa que ambos elementos son strings
    if all(son_strings):
        return True
    else:
        return False
    



def inicio_validar():

    while True:
        word1 = input('1 palabra: ')

        word2 = input('2 palabra: ')

        lista_ingresada = [word1, word2]

    # Validamos la lista con nuestra función
        if validar(lista_ingresada):
            print('\n✅ ¡Datos correctos! Has ingresado dos strings.')
            print('---')
            print('Las palabras ingresadas fueron:')

            # Imprimimos las palabras en minúsculas
            for p in lista_ingresada:
                print(p.lower())

            break  # Salimos del bucle si los datos son correctos

        else:
            # Este 'else' no se activará con 'input' ya que siempre retorna string
            # pero es útil si la función se usa con otros tipos de datos.
            print('❌ Error: Asegúrate de ingresar strings. Inténtalo de nuevo.\n')
            continue




inicio_validar()









