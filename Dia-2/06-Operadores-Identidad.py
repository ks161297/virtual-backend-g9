# is => es 
# is not => no es

frutas = ['carambola', 'guayaba', 'higo', 'melocoton']
fruta = 'carambola'

#Para poder ver en que posicion de la memoria esta siendo ubicada una variable se usa el metodo id()

print(id(fruta))
print(id(frutas))

#El 'is' e 'is not' se usa mas que todo para validar si las variables a comparar estan apuntando a la misma dirección de memoria o no
#Las variables que son colecciones de datos como listas, tuplas y diccionarios son variables mutables.
#Las otras variables(int, str, float) son variables inmurtables
frutas2 = frutas 
frutas2.append('fresa') #Agregar valor a la lista
print(frutas)
print(id(frutas2))
print(id(frutas))
print(frutas2 is frutas)

#Las dos variables NO COMPARTEN la misma ubicación de memoria

print(fruta is frutas)


#Variables mutables e inmutables
# Para hacer copia sin que se ubique en la misma posición de memoria, se hace uso de copu (metodo propio de listas) 
frutas_variadas = frutas.copy()
print(id(frutas_variadas))
print(id(frutas))
print(frutas_variadas is frutas)
