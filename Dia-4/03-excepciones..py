

try:
    numero = 5/1
    print(f"El numero es {numero}")
    numero = 1000/0
    # sumar = 1 + "1"
except ZeroDivisionError:
    print("Hubo un error al hacer la división")

except TypeError: 
    print("No se puede sumar entre strings y numeros")
except: 
    print("Error desconocido")
else: 
    print("Todo bien")
finally:
    print("Igual me ejecuto")

#Finally = no importa si la operación salió bien o hubo errores, igual se ejecutará.
#Else = para usar el else tenemos que obligatoriamente DECLARAR un except y este se ejecutará cuando no ingresa a ningun except(Cuando la operación no tuvo errores)

print("Soy un ejemplo ññ")

#Ingresar 4 numeros, si uno de ellos no es un número entonces no tomarlo en cuenta y volver a pedir hasta que tengamos los 4 números. 


numeros = []
while len(numeros) != 4:
    try:
        numero = int(input("Ingresa un número:"))
        numeros.append(numero) 
    except:
        pass

print("Los números son {}".format(numeros))