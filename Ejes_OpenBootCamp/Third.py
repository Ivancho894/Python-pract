#Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros),
#Calcule el índice de masa corporal y lo almacene en una variable, e
# imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.
# Tienes que subir capturas de pantalla en una carpeta comprimida zip.

def calculoMasaCorp():
    peso = float(input("Ingrese su peso en kilogramos por favor: "))
    altura = float(input("Ingrese su altura en la unidad de metros por favor: "))
    masaCorporal = peso/altura
    print ("Tu indice de masa corporal es: ", round(masaCorporal,2))
calculoMasaCorp()