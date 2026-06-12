# Variables en Python
#
# Las variables sirven para guardar datos en memoria.
# Python es lenguaje de tipado dinámico y de tipado fuerte.
###

# Para asignar una variable solo hace falta poner esto:
my_name = "sopedev"

print(my_name)


# Las variables se pueden resignar en tiempo de ejecución
age = 36
print(age)

#
age = 38
print(age)

# Tipado dinámico: el tiempo de dato se determina en tiempo de ejecución.
# No tienes que declararlo explícitamente.

name = "Sergio"
print(type(name))

print(" ")

name = 38
print(type(name))

# Tipado fuerte: Python no realiza conversión de tipado automático
# print(10 + "2")  # --> no puedes hacer esto en python

###
print(" ")


# f-string (Literal de cadena de formato)
# desde la versión Python 3.6
print(f"Hola {my_name}, tengo {age - 1} años.")

###
# No recomendado forma de asignar variables
name, age, city = "sergio", 36, "Oran"

print(name, age, city)

###
print(" ")
# Convención de nombre de variables
# snake_case
my_name_var = "ok --> varables en snake_case en python --> forma estandar"
print(my_name_var)

###
# PascalCase
MiNombreDeVariable = "PascalCase"

###
minombredevariable = "todojunto"

###
# Simular constante en Python
MI_CONSTANTE = 3.14  # UPPER_CASE -> constante

print(" ")

###

# Anotacion en Python
# Se puede hacer chequeó de tipos de datos
# para una mejor desarrolló
is_user_ligges_in: bool = True
print(is_user_ligges_in)

is_user_ligges_in = 14
print(is_user_ligges_in)
