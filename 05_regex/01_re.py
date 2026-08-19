###
# 01 - Expresiones regulares
###

"""
Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc."""

""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes 
  de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, 
  teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto 
  fácilmente
"""

# 1. Importar el módulo re
import re

text_1 = "\nExpresiones regulares:\n"
print(text_1.upper())

# 2. Crear un patron, que es una cadena de texto que describe el patrón
# que queremos buscar.

pattern = "Hola mundo"

# 3. El texto donde vamos a buscar el patrón
text_2 = "Hola mundo, este es un ejemplo de expresiones regulares. Hola mundo, este es otro ejemplo."

# 4. Usar la funcion de busqueda re "re"
result = re.search(pattern, text_2)


if result:
    print(f"Se encontró el patrón '{pattern}' en el texto.")
else:
    print(f"No se encontró el patrón '{pattern}' en el texto.")
