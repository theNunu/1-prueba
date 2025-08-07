def manipulando_frase(frase):
    print('tu frase echa array')
    frase = frase.split() #divide la frase elementos
    frase = set(frase)
    print (frase)
    frase = list(frase)
    print(frase)
    for f in frase:
        f = f.lower()
        print(f'es el elemento: {f}, tiene una longitud de {len(f)}')
        # if len(f) == len(f):
        #     print('este elemento coincide con la cantidad de otro elemento del array')


#eduARdo come en su casa, eduarDO cocina en su restaURANTE
print("programa que manipula una frase")

frase = input('ingresa la frase: ')
manipulando_frase(frase)
# word =len('deww')
# print(word)





