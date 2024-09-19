#Programa que solicita al usuario un número entero positivo y luego imprima los números desde ese número hasta 1 utilizando buclewhile  

def resultado():
    numero = int(input("Introduce un número entero positivo: "))

    if numero > 0:

        while numero >= 1:
            print(numero)
            numero -= 1  
    else:
        print("Introduce un número entero positivo.")

if __name__ == "__main__":
    resultado()