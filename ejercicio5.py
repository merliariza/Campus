"""Crea un programa que pida al usuario ingresar el nombre de un país y luego
determine en qué continente se encuentra.Utiliza estructuras condicionales para
asociar cada país con su respectivo continente y muestra un mensaje con el
continente correspondiente."""

def leercontinente():
    pais=input('Ingrese un país: ')
    if pais in ('argentina', 'brasil', 'colombia', 'perú', 'chile'):
        print ('El país es de América del Sur')
    elif pais in ('canadá', 'méxico', 'estados unidos'):
        print ('El país es de América del Norte')
    elif pais in('españa', 'francia', 'alemania', 'italia'):
        print ('El país es de Europa')
    elif pais in ('china', 'japón', 'india'):
        print ('El país es de Asia')
    elif pais in ('australia', 'nueva zelanda'):
        print ('El país es de Oceanía')
    elif pais in ('egipto', 'sudáfrica', 'nigeria'):
        print ('El país es de África')
    else:
        print ('El país no se encuentra')

if __name__ == "__main__":
    leercontinente()