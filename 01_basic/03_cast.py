# Casting de tipos de datos
# Transformar un tipo de dato a otro

print("\n Conversion de tipos de datos \n")
print("1000")
print(type("1000"))  # Es un string

print(type(int("1000")))

suma = 2 + int("5")
print(suma)
print(type(suma))

print("3.1416")
print(type("3.1416"))  # Es un string
pi = float("3.1416")
print(pi)
print(type(pi))

print(bool(0))  # False
print(bool(1))  # True
print(bool(-1))  # True

# False --> la unica cadena vacía es False, cualquier otra cadena es True
print(bool(""))
print(bool(" "))  # True --> tiene un espacio, no es una cadena vacía
print(bool("False"))  # True
