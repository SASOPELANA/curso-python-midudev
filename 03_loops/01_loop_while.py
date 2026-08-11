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

# else, esta condición cuándo se ejecuta?
print("\n ----- Bucle while con else ----- \n")
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle a termiando.")

# Pedirle al usuario un número que tiene
# que ser positivo

"""
numero = -1
while numero <= 0:
    numero = int(input("Escribe un número positivo: "))
    if numero <= 0:
        print("El número debe ser positivo. Intente otra vez.")

print(f"El número que has introducido es {numero}")
"""

# Manejó de Errores
numero = -1
while numero <= 0:
    try:
        numero = int(input("Escribe un número positivo: "))
        if numero <= 0:
            print("El número debe ser positivo. Intente otra vez.")
    except:
        print("Lo que introduces debe ser un número.")

print(f"El número que has introducido es {numero}")
