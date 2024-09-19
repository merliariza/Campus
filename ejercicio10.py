"""Construya un algoritmo en Python, que
permita ingresar la información de un
empleado e imprima el nombre, los apellidos
y la antigüedad. Los datos que se deben
solicitarson los siguientes:
*Nombre* Teléfono
*Año de ingreso a la empresa*Apellidos
*Edad."""

def datos():
    nombre = input('Ingrese el nombre: ')
    apellidos = input('Ingrese los apellidos: ')
    edad = int(input('Ingrese edad: '))
    telefono = int(input('Ingrese telefono: '))
    antiguedad = int(input('Digite el año de ingreso: '))

    # Imprimir el mensaje deseado
    print(f"El nombre es: {nombre} {apellidos}, tiene {edad} años, su teléfono es {telefono}, y tiene {antiguedad} años de antigüedad.")

if __name__ == "__main__":
    datos()