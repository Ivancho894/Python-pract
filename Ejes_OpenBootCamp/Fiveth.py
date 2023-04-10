#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.



def  bisiestoCheck(year):
    if (year%4 == 0) :
        print(year, "es bisiesto")
    else:
        print(year, "no es bisiesto")

inp = 1
while inp !=0:
    inp = int(input("Ingrese ano para verificar si es bisiesto (0 para finalizar): "))
    bisiestoCheck(inp)