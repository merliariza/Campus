#Programa que determina de acuerdo a una calificación, si el usuario ha aprobado o reprobado
def leercalificacion():
    calificacion= int(input('Ingrese una calificación: '))

    if calificacion >= 60:
        print('Ha sido aprobado')
    else:
        print('Ha sido reprobado')


if __name__ == "__main__":
    leercalificacion()