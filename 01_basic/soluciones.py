# Ejercicio 1: Imprimir mensajes
# Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.

print("\n ------- EJERCICIO 1 ------- \n")

name = "Sergio Alejandro Sopelana"
city = "Buenos Aires"

print(f"Tu nombre es {name} y eres de la Provincia de {city}")


# Ejercicio 2: Muestra los tipos de datos de las siguientes variables:
# Usa el comando 'type()' para determinar el tipo de datos de cada variable.

"""
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None
"""

print("\n ------- EJERCICIO 2 ------- \n")

a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print("Tipos de datos: ")
print("\n", type(a), "\n", type(b), "\n", type(c), "\n", type(d), "\n", type(e))

# Ejercicio 3: Casting de tipos
# Convierte la cadena "12345" a un entero y luego a un float.
# Convierte el float 3.99 a un entero. ¿Qué ocurre?

print("\n ------- EJERCICIO 3 ------- \n")

string_number = "123456"
print(type(string_number))
print(type(int(string_number)))

print(" ")

print(type(string_number))
print(type(float(string_number)))

print(" ")

num_float = 3.99
print(type(num_float))
print(type(int(num_float)))

num_int = int(num_float)
print(num_int)

explicacion = """
Explicación: Al convertir un float a int, Python TRUNCA (elimina) la parte decimal. 
3.99 -> 3 No redondea a 4, simplemente corta los decimales.
    """

print(explicacion)


print("\n ------- EJERCICIO 4 ------- \n")

# Ejercicio 4: Variables
# Crea variables para tu nombre, edad y altura.
# Usa f-strings para imprimir una presentación.

nombre = "Sergio"
edad = 36
altura = 1.79

print(f"Hola soy {nombre}, tengo {edad} años y mido {altura} m de altura.")

print("\n ------- EJERCICIO 5 ------- \n")

# Ejercicio 5: Números
# 1. Crea una variable con el número PI (sin asignar una variable)
# 2. Redondea el número con round()
# 3. Haz la división entera entre el número que te salió y el número 2
# 4. El resultado debería ser 1

result = int(round(3.1416) / 2)
print("Valor de PI (APROXIMADO): ", 3.1416)
print("PI redondeado: ", round(3.1416))
print("Division entera de PI con redondeado entre 2: ", result)
