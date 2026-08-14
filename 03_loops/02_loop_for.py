###
# 02 - Bucle (for)
# Permiten ejecutar un bloque de código repetidamente mientras
# Itera una lista
###

print("\n Buble for \n")

# Iterar una lista
frutas = ["manzana", "uva", "banana", "pera"]
for fruta in frutas:
    print(fruta)

# Iterar cobre culquier cosa que sea iterable
cadena = "sopedev"
for caracter in cadena:
    print(caracter)

# enumerate()
print("\nRange:")
frutas = ["naranja", "kiwi", "sandía", "cereza"]
for idx, value in enumerate(frutas):
    print(f"Índice: {idx}, Valor: {value}")

print("\nRange:")
# bucles anidados
letras = ["A", "B", "C", "D"]
numeros = [1, 2, 3, 4]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

print("\nBreak:")
# break
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"El loro esta escondido en el indice {idx}")
        break

print("\nContinue:")
# continue
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
    if animal == "loro":
        continue
    print(animal)

# Comprensión de listas (list comprehension)
print("\nList comprehension:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayusculas = [animal.upper() for animal in animales]
print("\nAnimales en mayúsculas:", animales_mayusculas)

# Muestra los números pares de una lista del 0 al 10 usando list comprehension
print("\nNúmeros pares de una lista:")
pares = [num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if num % 2 == 0]
print(pares)
