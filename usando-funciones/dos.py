

def asegurar_nombre(nombre):
    if len(nombre) > 4:
        print('el nombre es aceptable')
        return True
    else:
        print('el nombre no es valido')
        return False

def asegurar_conntrasena_coinciden(contrasena1, contrasena2):
    if contrasena1 == contrasena2:
        print('las contraseñas coinciden, BIEN HECHO')
        return True
    else:
        print('❌ Las contraseñas no coinciden. Inténtalo de nuevo.')
        return False
        
def asegurar_contrasena_longitud(contrasena):
    """
    Valida si la contraseña tiene al menos 8 caracteres.
    Retorna True si es válida, False en caso contrario.
    """
    if len(contrasena) >= 4:
        return True
    else:
        print('❌ La contraseña debe tener al menos 8 caracteres.')
        return False
    

def imprimir_datos_usuario(nombre, contrasena2):
    print(f'felicidades, tus datos de nombre: {nombre} y contrasena: {contrasena2} fueron aceptados')


def registro_usuario():

    print("""   
        |-------------------------|
        |    login en python      |
        |-------------------------|
        """)
    
    nombre_valido = False
    contrasena_valida = False
    contrasenas_iguales = False

    while True:
        if not nombre_valido:
            nombre = input('ingresa tu nombre: ')
            nombre_valido = asegurar_nombre(nombre)
            if not nombre_valido:
                continue # Vuelve al inicio del ciclo si el nombre es inválido
        
        if not contrasena_valida:
            contrasena1 = input('ingrese una contraseña: ')
            contrasena_valida = asegurar_contrasena_longitud(contrasena1)
            if not nombre_valido:
                nombre_valido = False # Si la contraseña es inválida, se reinicia la validación del nombre
                continue

        if not contrasenas_iguales:
            contrasena2 = input('asegura otra vez la contraseña: ')
            contrasenas_iguales = asegurar_conntrasena_coinciden(contrasena1, contrasena2)
            if not contrasenas_iguales:
                nombre_valido = False # Si no coinciden, se reinicia la validación completa
                contrasena_valida = False # Si no coinciden, se reinicia la validación completa
                continue
        

        # Si todas las validaciones son True, se imprime el mensaje final y se rompe el ciclo
        if nombre_valido and contrasena_valida and contrasenas_iguales:
            imprimir_datos_usuario(nombre, contrasena2)
            break


registro_usuario()









