"""Crea un programa que solicite al
usuario ingresar una contraseña y
verifique si cumple con los siguientes
requisitos: debe tener al menos 8
caracteres y contener al menos un
número. Si la contraseña cumple con
los requisitos, muestra el
mensaje"Contraseña válida". De lo
contrario, muestra el mensaje
"Contraseña inválida"."""

def leercontraseña():
    contraseña= input('Ingrese una contraseña')

    if len(contraseña) < 8:
        return False
    if not any(char.isdigit() for char in contraseña):
        return False
    return True

def resultado(valida):
    if valida:
        print('La contraseña es válida')
    else: 
        print('La contraseña es inválida')

if __name__ == "__main__":
    valida = leercontraseña()
    resultado(valida)