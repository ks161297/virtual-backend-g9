###### Condicionales 
# IF (si) (edad > 18) .... else .... 

edad = int(input("Ingresa tu edad"))
if (edad >= 18 and edad <= 64):
    print("Puedes vacunarte")
    print("Sigo en el if")
elif (edad >= 65 and edad <= 100):
    print("Necesitas segunda dosis")
else:
    print("Todavia no puedes vacunarte")


#print("Yo me ejecuto así se cumpla o no el if")

#OPERADOR TERNARIO

#Es una forma de hacer una validación pero en una sola línea de código
#R           ESULTADO_IF    IF CONDICION  ELSE    RESULTADO_ELSE     

texto = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(texto)

#Destructuración de variables una lista o tupla
# variable1, variable2, variable3, variable4 = ["hola", "como", "estas"]
#print(variable1)
#print(variable2)


#Ingresar un número y validar si es par, impar o 0

numero = int(input("Ingresa el número"))
if numero == 0: 
    print ("El número es 0")
elif numero % 2 == 0:
    print(f"El número {numero} es par")
else: 
     print(f"El número {numero} es impar")


#BUCLES

#FOR => repite desde hasta

meses = ['AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE','DICIEMBRE']

#Si nosotros queremos iterar una colección de datos la mejor forma es mediante un FOR

for mes in meses: 
#A diferencia del manejo de scopes(alcance) de la variable en JS, en python, la variable sigue existiendo fuera del for
    print(mes)
print ("*-------------------------------------------*")
#for(let i=0; i<10; i++){....}
for numero in range(10):
    print(numero)

#El range puede recibir hasta 3 parame
#range(n) => n: el limite de las iteraciones
#range (m,n) => m: el número inicial
print ("*-------------------------------------------*")
for numero in range (5 ,10):
    print(numero)
#range (m,n,o) => O: en cuanto se incrementa cada ciclo (valor)


print ("*-------------------------------------------*")
for numero in range (1,10,2):
    print(numero)



print ("*--------------------------Ejercicio-----------------------------*")


#De la siguiente lista de número indicar cuantos son positivos y negativos

numeros = [-4, 7, - 10, 8, 25, -7, -10]

# RPTA:
# Hay 3 negativos y 3 positivos
positivos = 0
num_positivos = []
negativos = 0
num_negativos = []

for numero in numeros:
    if(numero > 0):
        num_positivos.append(numero)
        positivos += 1
    else:
        num_negativos.append(numero)
        negativos += 1


print(f"Hay {negativos} negativos y son {num_negativos} y {positivos} positivos y son {num_positivos}")


num_positivos = []
num_negativos = []

for numero in numeros:
    if(numero > 0):
        num_positivos.append(numero)
    else:
        num_negativos.append(numero)

print(f"Hay {len(num_negativos)} negativos y son {num_negativos} y {len(num_positivos)} positivos y son {num_positivos}")


resultado = [[], []]
for numero in numeros:
    if(numero > 0):
        resultado[0].append(numero)
    else:
        resultado[1].append(numero)

print(
    f"Hay {len(resultado[1])} negativos y son {resultado[1]} y {len(resultado[0])} positivos y son {resultado[0]}")

print("=============================")
# BREAK
# hace que el bucle finalice de manera inesperada
for segundo in range(60):
    print(segundo)
    if segundo == 10:
        break

# NOTA: en Python el switch - case no existe!.

print("=============================")
# CONTINUE
# salta la iteracion actual
for numero in range(15):
    if numero == 10 or numero == 11 or numero == 12:
        continue
    print(numero)

print("=============================")
# dado los siguientes numeros:
numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]
# indicar cuantos de ellos son multiplos de 3 y de 5 , ademas si hay un multiplo de 3 y de 5 no contabilizarlos
# multiplos de 3: 3 , multiplos de 5: 1

multiplos_3 = 0
multiplos_5 = 0

for numero in numeros:
    if numero % 15 == 0:
        continue
    elif numero % 3 == 0:
        multiplos_3 += 1
    elif numero % 5 == 0:
        multiplos_5 += 1

print(f"Multos de 3 {multiplos_3}, multiplos de 5 {multiplos_5}")

print("=============================")
# WHILE (mientras)
# se ejecutara siempre que la condicion sea verdadera
# NOTA: en Python no existe el do-while

numero = 5
while numero < 10:
    numero += 1
    print(numero)

print("=============================")

# ingresar numeros hasta que ese numero sea adivinado
numero_adivinar = 10
# 5 => 'el numero es mayor que ese'
# 13 => 'el numero es menor que ese'
# 10 => 'felicidades adivinaste el numero'


numero_adivinar = 10
intento = 0
while intento < 10:
    numad = int(input("Ingresa un número"))
    intento = intento + 1 
    if numad > numero_adivinar:
        print(f"El número ingresado{numad} es mayor. ¡Prueba de nuevo!")
    if numad < numero_adivinar:
        print (f"El número ingresado {numad} es menor. ¡Prueba de nuevo!")
    if numad == numero_adivinar: 
        print(f"el numero {numad} es igual al numero a adivinar {numero_adivinar} , ¡Lo hiciste! en {intento} intentos")
        break