###

# 05 - Entrada de usuario (input()) - Versión simplificada
# La función input() permite obtener datos del usuario a través de la consola.

###

# Imprime un mensaje solicitando el nombre del usuario
print("Hola, Como te llamas?\n")
name = input()

print(f"Hola {name}, es un placer conocerte!")

age = input("¿Cuantos años tienes?\n")

print(f"Tienes 20 años, otra edad: {int(age) + 3}")

print(" ")

# Separar lista con split()
print("Obtener multiples valores a la vez.")
country, city = input("¿En que pais y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")
