"""Crea un programa que solicite al
usuario un número entero positivo y
luego imprima los números desde ese
número hasta 1 utilizando un
buclewhile."""

def leernumero():
    while True:
        numero= int(input('Ingrese un número: '))
        if numero > 0:
            return numero
        else:
            print("Por favor, ingrese un número entero positivo.")
        
        while numero >= 1:
            print(numero)
            numero -= 1


if __name__ == "__main__":
   leernumero()

