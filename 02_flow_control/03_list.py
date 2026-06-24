###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos, incluyendo otras listas.
###

print("\n ----- Listas en Python ----- \n")

# Listas de enteros
list_1 = [1, 2, 3, 4, 5]

# listas de cadenas de string
list_2 = ["peras", "sandia", "bananas", "naranja"]

# Listas de tipos mixtos
list_3 = [1, "hola", 3.14, True]

# Listas vacias
list_4 = []

# Listas de listas
list_5 = [[1, 2], [2, 3]]

# Matrix
matrix = [[1, 2], [2, 3], [4, 5]]

print(list_1)
print(list_2)
print(list_3)
print(list_4)
print(list_5)
print(matrix)

print("\nAcceso a elementos por índice.\n")
print(list_2[1])  # --> sandia
print(list_2[0])  # --> peras

# Acceder a índices de forma negativa
print(list_2[-1])  # --> naranja
print(list_2[-2])  # --> bananas

print(" ")

# Acceso a listas de listas
print(list_5[1][1])  # --> 3
