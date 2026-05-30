# Tipos de datos en Python
# Python tiene varios tipos de datos
# int, float, str, bool, list, tuple, dict, set, NoneType, dict, range
# complex ...

"""
Comentarios de varias lineas
Puede ser usando doble comilla o comilla simple
Sirve para explicar el codigo, o para escribir notas, documentacion, etc.
"""

# Numeros enteros (int)
print("\n Números Enteros --> int \n")
print(10)
print(0)
print(-5)

print(" ")

# Ver el tipo de dato
print(type(20))
print(7245984584102145023654123)
print(type(7245984584102145023654123))
print(7245984584102145023654123 + 5)

# Numeros decimales (float)
print("\n Números Decimales --> float \n")

print("float: ")
print(3.14)
print(type(3.14))
print(0.0)
print(type(0.0))
print(1e3)  # Anotación científica, equivalente a 1000.0
print(type(1e3))
print(-5.52)
print(type(-5.52))


print("\n Números Complejos --> complex \n")

# Para cientificos, ingenieros, etc.
print("complex: ")
print(1 + 2j)
print(type(1 + 2j))

print("\n Cadenas de texto --> str \n")

print("str: ")
print("Hola, mundo!")
print(type("Hola, mundo!"))
print("123456")
print(type("123456"))
print("""Multiple\nLineas\nDe\nTexto""")
print(type("""Multiple\nLineas\nDe\nTexto"""))

print("\n Bool - Banderas --> bool \n")
print("bool: ")
print(True)
print(type(True))
print(False)
print(type(False))
print(1 > 2)  # Es una expresión que evalúa a False
print(type(1 > 2))
print(5 == 5)  # Es una expresión que evalúa a True
print(type(5 == 5))

# Valor ausente de valores (NoneType)
print("\n Valor Ausente --> NoneType \n")

print("NoneType: ")
print(None)
print(type(None))
