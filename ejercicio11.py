11
def total():
    consumo = input("Ingrese el mes de consumo: ")
    valorkw = float(input("Ingrese el valor del kW: "))
    totalkw = float(input("Ingrese el total de kW consumidos en el mes: "))
    estrato = input("Ingrese el estrato: ")

    valorTotal = valorkw * totalkw

    print(f"\nMes de consumo: {consumo}")
    print(f"Valor por kW: {valorkw}")
    print(f"Total kW consumido: {totalkw}")
    print(f"Estrato: {estrato}")
    print(f"Valor a pagar por energía eléctrica: {valorTotal}")

if (__name__ == "_main_"):
  total()