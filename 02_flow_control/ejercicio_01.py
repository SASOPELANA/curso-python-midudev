###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4,
# excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

# Ejercicio 1
def ejercicio_1():
    print("\n ******* Ejercicio 1: Determinar el mayor de dos números *******\n")

    print("Ingresa un número: ")
    num_1 = int(input())

    print("Ingresa otro número: ")
    num_2 = int(input())

    if num_1 > num_2:
        print(f"El número {num_1} es mayor al número {num_2}")
    elif num_2 > num_1:
        print(f"El número {num_2} es mayor al número {num_1}")
    else:
        print("Los números son iguales.")


# Ejercicio 2
def ejercicio_2():
    print("\n ******* Ejercicio 2: Calculadora simple *******\n")

    n1 = float(input("Ingrese un número: "))
    n2 = float(input("Ingrese otro número: "))
    operacion = input(
        "\nElije el signo de la operación Aritmética:\nSuma --> +\nResta --> -\nMultiplicación --> *\nDivisión --> /\n"
    )

    if operacion == "+":
        suma = n1 + n2
        print(f"La suma es: {suma}")
    elif operacion == "-":
        resta = n1 - n2
        print(f"La resta es: {resta}")
    elif operacion == "*":
        multi = n1 * n2
        print(f"La multiplicación es: {multi}")
    elif operacion == "/":
        if n2 == 0:
            print(f"No se puede dividir entre {int(n2)}")
        else:
            division = n1 / n2
            print(f"La división es: {division}")
    else:
        print("Operación no valida.")


# Ejercicio 3
def ejercicio_3():
    print("\n ******* Ejercicio 3: Año bisiesto *******\n")
    anio = int(input("Ingrese el año: "))

    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        print(f"{anio} es un año bisiesto.")
    else:
        print(f"{anio} no es un año bisiesto.")


# Ejercicio 4
def ejercicio_4():
    print("\n ******* Ejercicio 4: Categorizar edades *******\n")

    age = int(input("Ingrese la edad: "))

    if age >= 0 and age <= 2:
        print("Bebé.")
    elif age >= 3 and age <= 12:
        print("Niño.")
    elif age >= 13 and age <= 17:
        print("Adolescente.")
    elif age >= 18 and age <= 64:
        print("Adulto.")
    elif age >= 65:
        print("Adulto mayor.")
    else:
        print("Edad no valida.")


###
# Llamar la funcion con el ejercicio
# ejercicio_1()
# ejercicio_2()
# ejercicio_3()
# ejercicio_4()

opcion = input("¿Qué ejercicio querés ejecutar? (1/2/3/4): ")

if opcion == "1":
    ejercicio_1()
elif opcion == "2":
    ejercicio_2()
elif opcion == "3":
    ejercicio_3()
elif opcion == "4":
    ejercicio_4()
else:
    print("Opción no válida.")
