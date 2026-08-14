###
# 03 - range()
# Permite crear una secuencia de números, que se puede recorrer con un bucle for.
# pero no solo eso
###

print("\nrange():\n ")
nums = range(10)
print(nums)

for num in nums:
    print(num + 1)


print("\nrange(inicio, fin):\n ")
# range(inicio, fin)
for num in range(5, 10):
    print(num + 1)

print("\nrange(inicio,fin,paso):\n ")
for num in range(0, 10, 2):
    print(num + 1)


print("\nrange con negativos:\n ")
# range con negativos
for num in range(-10, 0):
    print(num)

print("\nrange con decrementó:\n ")
for num in range(10, 0, -1):
    print(num)

# crea listas a partir de un rango
print("\nCrear listas a partir de un rango:\n ")
nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

print("\n")
# recorrer un rango con un bucle for
for _ in range(6):
    print("Hola mundo")
