
def triangulo():
    a = float(input("Ingrese la primera longitud: "))
    b = float(input("Ingrese la segunda longitud: "))
    c = float(input("Ingrese la tercera longitud: "))

    if a + b > c and a + c > b and b + c > a:
        print("Pueden formar un triángulo válido.")
    else:
        print("NO pueden formar un triángulo válido.")


if (__name__ == "__main__"):
    triangulo()