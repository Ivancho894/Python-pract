#Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista.
# No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados
# alfabéticamente y separados por comas.









def muestraPaises(paises):
    #STR to Array
    arrPaises = paises.split(', ')
    #check if there is any duplicated
    setPaises = set(arrPaises)
    #sort them
    ordPaises = sorted(setPaises)
    print(", ".join(ordPaises))

def main():
    paises = input("Ingrese los paises separados por ,")
    muestraPaises(paises)

main()