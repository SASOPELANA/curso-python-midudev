###
# Métodos
###

# 04 - Listas métodos
# Los métodos mas importantes para trabajar con listas son:

# Añadir o insertar elementos a la lista
print("Metodos de listas\n")
lista1 = [1, 2, 3, 4, 5]

# Añadir elementos al final de lista
lista1.append(6)
print(lista1)

# Insertar un elemento en la posición que le indiquemos como
# primer argumento

lista1.insert(1, 22)
print(lista1)

# Agregar elementos al final de la lista
lista1.extend([7, 8])
print(lista1)

# Eliminar elementos de la lista
# Eliminar el primer 22 en la aparición de la lista
lista1.remove(22)
print(lista1)

# Eliminar el ultimo elemento  de la lista y lo
# ademas lo devuelve.
ultimo = lista1.pop()
print(ultimo)
print(lista1)

# Eliminar el segundo elemento de la lista
# (indice 1)
lista1.pop(1)
print(lista1)

# otro método para eliminar elementos
del lista1[-1]
print(lista1)

# Eliminar todos los elementos de la lista
lista1.clear()
print(lista1)

# Eliminar un rango de elementos
lista1 = ["panda", "gato", "conejo", "tigre", "perro"]
del lista1[1:3]
print(lista1)

print(" ")

# Métodos útiles
print("Ordernar listas modificando la original")
numbers = [3, 12, 1, 2, 5, 90, 10]
numbers.sort()
print(numbers)

print("\nOrdernar listas creando una nueva lista")
numbers = [3, 12, 1, 2, 5, 90, 10]
sorter_numbers = sorted(numbers)
print(sorter_numbers)

print(" ")
# Ordenar listas de cadena de textos
print("Ordernar una lista de cadenas de texto (todo minúsculas)\n")
frutas = ["banana", "pera", "manzana", "uva", "durazno", "naranja"]
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print(" ")
# Ordenar listas de cadena de textos
print("Ordernar una lista de cadenas de texto (mezclas mayúsculas y minúsculas)\n")
frutas = ["banana", "Pera", "Manzana", "uva", "durazno", "Naranja"]
sorted_frutas = sorted(frutas)
print(sorted_frutas)
