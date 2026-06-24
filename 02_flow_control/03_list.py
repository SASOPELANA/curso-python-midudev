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

# Slicing (rebanado) de listas
print("\nRebanado de listas en Python \n")
list_1 = [1, 2, 3, 4, 5, 6]
print(list_1[1:5])  # [ 2,3,4,5 ]
print(list_1[:3])  # [ 1,2,3]
print(list_1[3:])  # [4, 5, 6]
print(list_1[:])  # [1, 2, 3, 4, 5, 6]

# list_1[desde:hasta] --> como funciona el rebanado
# list_1[desde:hasta:paso] --> rebanado con paso

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# paso de dos en dos con rebanado
print(list_1[::2])

# paso de tres en tres con rebanado
print(list_1[::3])

# revertir lista
print(list_1[::-1])  # revierte la lista
