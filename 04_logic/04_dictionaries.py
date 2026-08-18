###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor,
# donde cada clave es única y se utiliza para acceder a su valor correspondiente.
# Los diccionarios son mutables, lo que significa que se pueden modificar
# después de su creación.
###

# Ejemplo de diccionario
text_1 = "\n ----- Diccionarios en Python ejemplos ----- \n"
print(text_1.upper())

person_1 = {
    "name": "Sergio",
    "age": 30,
    "is_student": True,
    "califications": [8.5, 9.0, 7.5],
    "social_media": {
        "twitter": "@sergio",
        "instagram": "@sergio_insta",
        "facebook": "sergio.fb",
        "portal": "sergio.com",
    },
}

print(person_1)
print(" ")
print(person_1["name"])  # Acceder al valor de la clave "name"
print(" ")
print(
    person_1["califications"][1]
)  # Acceder al segundo elemento de la lista "califications"
print(" ")
print(person_1["social_media"])

print(" ")

# Eliminar completamente una propiedad del diccionario
del person_1["age"]
# print(person_1)
#
print(" ")

# También se puede eliminar una propiedad del diccionario utilizando el método pop(),
# y lo recupera en una variable para su posterior uso.
is_student = person_1.pop("is_student")
print(f"is_student: {is_student}")
print(person_1)

print(" ")

# Sobreescribir un diccionario con otro diccionario
p1 = {"name": "Juan", "age": 33}
p2 = {"name": "Jose", "is_student": True}

p1.update(p2)
print(p1)

# Comprobar si existe una propiedad en un diccionario
text_ckeck = "\nComprobar si existe una propiedad en un diccionario \n"
print(text_ckeck.upper())
print("name" in person_1)  # True
print("is_philosopher" in person_1)  # False

# Obtener todas las claves de un diccionario
text_key = "\nMostrar todas las claves de un diccionario \n"
print(text_key.upper())
print(p2.keys())

# Obtener todos los valores de un diccionario
text_value = "\nMostrar todos los valores de un diccionario\n"
print(text_value.upper())
print(p1.values())

# Mostrar todas las claves y valores de un diccionario
print("\nMOSTRAR CLAVES Y VALORES DEL DICCIONARIO: \n")
for key, value in person_1.items():
    print(f"{key}: {value}")
