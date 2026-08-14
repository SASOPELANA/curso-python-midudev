###
# 04 - Funciones
# Bloque de código reutilizable que realiza una tarea específica.
###

"""
def name_function(parametro1, parametro2, ...):
    # docstring
    # cuerpo de la función
    # return valor_de_retorno --> opcional

"""

print("\n04 - Funciones\n")


# Ejemplo de una función para imprimir un mensaje por consola
def saludar():
    print("¡Hola, buenos dias!")


# funcion con parámetros
def saludar_a(name):
    print(f"Hola {name}")


saludar_a("sope")
saludar_a("Juan Luna")
saludar_a("Ricardo Pepe")

print("\nCreando una función que retorne un valor\n")


def sumar(a, b):
    return a + b


print(sumar(5, 3))
print(sumar(10, 20))

print("\nDocumentación de funciones con docstring: \n")

# Documentación de funciones con docstring


def restar(a, b):
    """Resta dos numeros y retorna el resultado."""
    resta = a - b
    return resta


resultado = restar(10, 5)
print(f"El resultado de la resta es: {resultado}")

print(restar.__doc__)  # --> muestra la documentación de la función restar

# help(restar)  # --> muestra la documentación de la función restar --> ayuda

# parámetros por defecto
print("\nParámetros por defecto\n")


def multiplicar(a, b=2):
    return a * b


print(multiplicar(2))  # --> 4
print(multiplicar(2, 3))  # --> 6

# Argumentos por posición
print("\nArgumentos por posición: \n")


def describir_persona(name, age, city):
    print(f"Nombre: {name}, Edad: {age}, Ciudad: {city}")


describir_persona(name="Juan Luna", age=33, city="San Ramón de la Nueva Orán")

# Argumentos por clave
# Parámetros nombrados
print("\nArgumentos por clave y parámetros nombrados: \n")

describir_persona(city="San Ramón de la Nueva Orán", name="Juan Luna", age=33)
describir_persona(city="Pichanal - Salta", name="Nicolas Perez", age=25)
