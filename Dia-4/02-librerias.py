# pip install camelcase

from camelcase import CamelCase

instancia = CamelCase("alumnos")

texto = "Hola alumnos buenas noches"

resultado = instancia.hump(texto)

print(resultado)

#pip freeze = ver librerías 
