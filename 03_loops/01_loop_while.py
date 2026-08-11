###
# 01 - Bucles - While
# Permiten ejecutar un bloque de código mientras se cumpla una condición.
###

print("\n ----- Bucle While ----- \n")

# Bucle con una simple condición.
contador = 0
while contador <= 5:
    print(contador)
    contador += 1

print("\n ----- Bucle While con break ----- \n")
# Salir del bucle con el break
cont = 0
while True:
    print(cont)
    cont += 1
    if contador == 6:
        break

print("\n ----- Bucle con continue ----- \n")
# continue, que lo hace es saltar esa iteración en concreto
# y continua con el bucle o ejecución
contador = 0
while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue

    print(contador)
