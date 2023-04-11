from functools import reduce


#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por
#parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.



def main():
    cant = input("Cantidad de datos a ingresar:")
    arr = []
    for a in range(0,int(cant)):
        arr.append(int(input("Ingrese dato: ")))
    #save only odd numbers
    arr = filter(lambda x: x%2!=0,arr)
    #add all values
    sum= reduce(lambda a,b: a+b,arr)
    print("La suma de los valores impares de los datos ingresados es: ",sum )

main()