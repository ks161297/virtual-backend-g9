# Una función es un bloque de código que se va a ejecutar, cuántas vece sea llamada la función.

def saludar():
    print("Hola, Buenas Tardes :)")

saludar()

def saludarpersona(nombre):
    edad=40
    print(f"Hola {nombre}, ¿Cómo te va?")

saludarpersona("Kimberly")

def sin_nombre():
    """Función que no hace nada y solamente es de muestra"""
    print("Yo soy una función sin nombre")

sin_nombre()

#Las funciones pueden recibir parámetros y estos pueden ser opcionales
def registro(nombre, correo=None):
    print("Registro Exitoso")

registro("Kimberly")
registro("Kimberly","mksss161297@gmail.com")
# registro()

# Crear una función llamada identificación en la cual se reciba el nombre y la nacionalidad del cliente, si en el caso no se pasa la identificación será peruana.


def identificacion(nombre, apellido, nacionalidad=None):
    if nacionalidad is None:
        print (f"La persona que ingreso fue {nombre}, {apellido} y es Peruan@")
    else: 
        print(f"La persona que ingreso fue {nombre}, {apellido} y es {nacionalidad}")

identificacion("Kimberly","Silva")
identificacion("Sofia","Herrera","Brasileño")

#Otra solución 

def identificacion_2(nombre, apellido, nacionalidad="Peruano"):
    resultado = {
        "nombre" : nombre,
        "apellido" : apellido,
        "nacionalidad":nacionalidad
    }
    print(resultado)

identificacion_2("Kimberly", "Silva","Coreana")
identificacion_2("Sue", "Solis")

#Todos los parámetros que tengan un valor predeterminado SIEMPRE van al final.
def sumatoria(num1, num2=10, num3=15):
    print(num1+num2+num3)

sumatoria(10)


#El parámetro que tiene el simbolo * es una parámetro especial de python que sirve para almacenar n valores.
#TODOS los valores que pasemos a ese parámetro se almacenaráb en una tupla en el mismo orden con el cual hemos pasado los parámetros.
def alumnos(*args):
    print(args)

alumnos("A","B","C","D","E","F","G","H","I")

def tareas(nombre, *args):
    print("OK :)")

tareas("Kimberly",1)

#Ejemplo 2 

def tareas_2(nombre, *args, apellido):
    print("OK :)")
    
tareas_2("Kimberly","1","2",3, apellido="martinez")

#Ejemplo 3 
def tareas_3(nombre, apellido, *args):
    print("OK :)")
    
tareas_3("Kimberly","Silva", "1","2", 3)

#En la función alumnos_notas se recibirá una cantidad N de alumnos en la cual se debe indicar cuantos aprobaron y cuantos desaprobaron siendo la nota minima 11. 


def alumnos_notas(*args):
    #todo implementar lógica
    aprobados = 0
    desaprobados = 0
    for alumno in args:
        if alumno['promedio'] > 10:
            aprobados +=1
        else:
            desaprobados +=1
    print(f"Hay {aprobados} alumnos aprobados y {desaprobados} alumnos desaprobados")

alumnos_notas(
    {"nombre" : "A", "promedio" : 17},
    {"nombre" : "B", "promedio" : 20},
    {"nombre" : "C", "promedio" : 10},
    {"nombre" : "D", "promedio" : 8},
    {"nombre" : "E", "promedio" : 16},
    {"nombre" : "F", "promedio" : 11}
)

#

def indeterminada(**kwargs):
    print(kwargs)
indeterminada(nombre="Kimberly", apellido="Silva", nacionalidad = "Peruano")
indeterminada(edad=50, estatura=1.55)

def variada(*args, **kwargs):
    print(args)
    print(kwargs)

variada(10, "Kimberly", {"est_civil": "Soltera"}, mascota="Buggie", raza="criollo")

def sumatoria(num1, num2):
    return num1+num2
    print("Otra cosa")

rpta = sumatoria(10,5)