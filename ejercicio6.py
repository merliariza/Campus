"""Escribe un programa que solicite al usuario ingresar el día, el mes y el año de
una fecha. Luego, verifica si la fecha es válida o no. Considera los diferentes
casos, como los días de cada mes y si el año es bisiesto. Muestra un mensaje
indicando si la fecha es válida o no."""

def bisiesto(año):
    restoUno= año%4
    restoDos= año%100
    restoTres= año%400
    if restoUno==0 and restoDos != 0:
        print('El año es bisiesto')
    elif restoTres==0 :
        print('El año es bisiesto')
    else: print('El año no es bisiesto')


def fecha(dia, mes, año):
    if mes < 1 or mes > 12:
        print("La fecha no es válida.")
    elif mes == 2:
        if bisiesto(año):
            if 1 <= dia <= 29:
                print("La fecha es válida.")
            else:
                print("La fecha no es válida.")
        else:
            if 1 <= dia <= 28:
                print("La fecha es válida.")
            else:
                print("La fecha no es válida.")
    elif mes in [4, 6, 9, 11]:
        if 1 <= dia <= 30:
            print("La fecha es válida.")
        else:
            print("La fecha no es válida.")
    else:
        if 1 <= dia <= 31:
            print("La fecha es válida.")
        else:
            print("La fecha no es válida.")

def main():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    
    fecha(dia, mes, año)

if __name__ == "__main__":
    main()