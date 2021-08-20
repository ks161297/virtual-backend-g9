# List => LISTAS
#Ordenadas y modificables 

colores = ['morado', 'azul', 'rosado', 'amarillo']
mezclada = ['otoño', 14, False, 15.2, [1,2,3]]

#imprimir 1era posicion 
#En Python si la posicion no existe, da error != JS 
print(colores[0])

#Al usar valores negativos en las posiciones de la lista, se 'invertira' y podremos recorrer dicha lista 

print(colores[-4])

# Las posiciones que sean desde la 1 hasta < 3
print(colores[1:3])

#toda las lista hasta la posicion < 2 

print(colores[:2])

#Sirve para copiar EL CONTENIDO de la lista, no la ubicación de memoria
colores_2 = colores[:]
print(id(colores_2))
print(id(colores))

print(colores[1:-1])

#metodo para agregar un elemento a una lista 
colores.append('naranja')
print(colores)

#metodo para eliminar un valor
#1. solamente si existe lo eliminara, sino lanzará un error

# colores.remove('azul')
# print(colores)

# 2. Si queremos eliminarlo y ADEMAS guardar el valor eliminado en una variable

color_eliminado = colores.pop(0)
print(colores)
print(color_eliminado)

#3. El metodo para eliminar el valor 
#Este metodo también sirve para eliminar variables

# nombre = "Kimberly"
# del nombre
# print(nombre)

del colores[0]
print(colores)

#sacar la longitud de la lista 

print(len(colores))


##TUPLAS
#La tupla a diferencia de la lista es una colección de datos ordenada PERO que una vez creada no se puede editar.

notas = (10, 15, 20, 9, 17)
print(notas[0])
print(len(notas))

print(notas.count(10)) #Cuantas veces se repite un elemento{{


#DICCIONARIOS 

persona = {
    'nombre' : 'Marigrace',
    'apellido' : 'Silva',
    'correo' : 'mksss161297@gmail.com',
    'edad' : 23,
    'donacion_organos' : False,
    'hobbies' : [
        {
            'nombre' : 'Pintar',
            'conocimiento' : 'Avanzado'
        },
        {
            'nombre' : 'Programar',
            'conocimiento' : 'Intermedio'
        }
    ]
}

persona['edad'] = 24
persona['nacionalidad'] = 'peruana'

print(persona["edad"])
print(persona['nombre'])
print(persona)

#Imprimir el primer hobby de la persona 

print(persona['hobbies'][0]['nombre'])

#forma de extraer solamente llaves 

print(persona.keys())

#forma de extraer solamente los valores

print(persona.values())

persona.clear()
print(persona)



##CONJUNTOS 
# Colección de datos DESORDENADA, que una vez que la creamos no podremos acceder a sus posiciones ya que estará ordenada aleatoriamente.

alumnos = {'Kevin', 'Kat', 'Kimberly', 'Jose','Ramiro', 'Sara'}
print(alumnos)
alumnos.add('Diego')
print(alumnos)
alumnos.remove('Jose')
print(alumnos)


# Se usa para guardar valores sin la necesidad de llaves 
cursos = {'matematica', 'cta', 'biologia','comunicacion'}
print('matematicas' in cursos)