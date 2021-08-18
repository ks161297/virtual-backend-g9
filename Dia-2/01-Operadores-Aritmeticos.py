num1 = 10
num2 = 80

persona1 = "Kimberly"
persona2 = "Marigrace"
#Suma

print(num1+num2) #Si las variables son numéricas se realiza la operación.
print(persona1+persona2) #Si las variables son string(carácter) se concatena
#print(num1+persona1) -> Error

#Conversión de un numérico a string
numero1_string = str(num1)
print(numero1_string+persona1)

#Resta
print(num1-num2)
print(num2-num1)

#print(persona1-persona2) -> Error

#Multiplicación
print("La multiplicación de 10 y 80 es:",num1*num2)

print("La multiplicación de {} y {} es: {}".format(num1,num2,num1*num2))


#División
print(num1/num2)
print(num2/num1)
#Modulo

print(num1%num2)
print(num2%num1)

#Cociente 

print(num2 // num1)