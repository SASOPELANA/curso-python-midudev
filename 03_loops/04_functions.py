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
