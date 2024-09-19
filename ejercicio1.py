#Programa que solicita al usuario la edad y determina si es o no mayor de edad.
def leeredad():
    edad= int(input('Ingrese la edad: '))


    if edad>=18:
        print('Es mayor de edad')
    else:
        print('Es menor de edad')



if __name__ == "__main__":
    leeredad()