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
