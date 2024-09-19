"""Crea un programa que solicite al usuario
ingresar una serie de números positivos y
luego calcule e imprima el promedio de los
números ingresados utilizando un bucle while.
El programa debe terminar cuando el usuario
ingrese un número negativo."""

def resultado():
    suma = 0
    contador = 0

    while True:
        numero = float(input("Ingresa un número positivo para promediar: "))
        
        if numero < 0:
            break
        
        suma += numero
        contador += 1

    if contador > 0:
        print("Promedio:", suma / contador)
    else:
        print("No se ingresaron números positivos.")

if __name__ == "__main__":
    resultado()