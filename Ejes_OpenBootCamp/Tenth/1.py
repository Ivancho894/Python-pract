#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo.
# Para ello, tendréis que acceder dos veces al archivo creado.
f = open ('arch.txt','w')
f.write('Hola que tal')
f.close()



p = open('arch.txt','r')
print(p.read())
p.close()