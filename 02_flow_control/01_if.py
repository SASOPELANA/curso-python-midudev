###
# Condicionales en Python
# 01 - Sentencia condicional (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumple una condiciones.
###

###
print("\n ------ CONDICIONALES ------\n")

print("Sentencia simple condicional\n")

age = 18

if age >= 18:
    print("Eres mayor de edad.")
    print("¡Felicidades!")

age = 15

if age >= 18:
    print("Eres mayor de edad.")
    print("¡Felicidades!")

print("\nCondicional con else")

age = 15
if age >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

print("\nSentencia condicional con elif")

note = 9
if note >= 9:
    print("¡Sobresaliente!")
elif note >= 7:
    print("Notable.")
elif note >= 5:
    print("¡Aprobado!")
else:
    print("¡Reprobado!")

print("\nCondicionales Múltiples\n")

edad = 25
tiene_carnet = False

if edad >= 18 and tiene_carnet:
    print("Puedes conducir un vehículo.")
else:
    print("No puedes conducir un vehículo.")

# La ciudad de # San Ramón de la Nueva Orán permite conducir
# a personas mayores de 18 años o que tengan carnet de conducir
print(" ")
if edad >= 18 or tiene_carnet:
    print("Puede conducir en la ciudad de San Ramón de la Nueva Orán.")
else:
    print("No puede conducir en la ciudad de San Ramón de la Nueva Orán.")

print(" ")

# Negacion de una condicion --> operador not
es_fin_de_semana = False
if not es_fin_de_semana:
    print("¡No es fin de semana, a trabajar!")

print("\nAnidar condicionales\n")

edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes salir a divertirte.")
    else:
        print("No tienes dinero para salir.")
else:
    print("Puedes salir a divertirte, pero necesitas ser mayor de edad.")

if edad < 18:
    print("No puedes salir a divertirte, necesitas ser mayor de edad.")
elif tiene_dinero:
    print("Puedes salir a divertirte.")
else:
    print("Quedate en casa, no tienes dinero para salir.")

print(" ")

numero = 5
if numero:
    print("El número es diferente de cero.")

name = "Juan"
if name:
    print("El nombre no está vacío.")

numero = 7
if numero == 3:
    print("El número es 3.")
else:
    print("El número no es igual.")

print("\n ----- Condición Ternaria ----- \n")
###
# Es una forma concisa de un if-else, en una linea de codigo.
# [Codigo se cumple la condicion] if [condicon] else [Codigo si no se cumple]
edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)
