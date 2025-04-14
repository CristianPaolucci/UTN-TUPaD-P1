#Ejercicio1

for x in range (0, 101, 1):    #Se utiliza ciclo for para que se muestre por pantalla lista de números del 0 al 100 incluidos
    print (x)  #SE imprime por pantalla dicha lista


#Ejercicio2

numero = input("Ingrese un número entero: ") #Se pide a usuario que ingrese un número entero

cant_digitos = len(numero) #Se utiliza la función len()para determinar cantidad de dígitos que contiene el número ingresado.
                           
print ("La catidad de dígitos ingresados es ", cant_digitos)  #Se imprime por pantalla resultado


#Ejercicio3

num1 = int(input("Ingrese el primer número entero: "))   #Se solicita a usuario que ingrese un número entero
num2 = int(input("Ingrese el segundo número entero: "))  #Se solicita a usuario que ingrese un número entero

if num1 > num2:  #Se compara números ingresados para chequear que el primer número ingresado no sea mayor que el segundo
    print("El primer número que ingrese debe ser menor que el segundo") #Se imprime por pantalla la condición a cumplir en el ingreso de número

for suma in range (num1+1, num2): #Se utiliza ciclo for para sumar valores entre dos números ingresados por usuario, excluyendo dichos números ingresados
    print (suma)  #Se imprime por pantalla resultado

#Ejercicio4

numero = int(input("Ingrese un número: ")) #Se solicita a usuario que ingrese un número entero
suma = 0  #Se asigna valor a la variable

while numero != 0:  #Se utiliza ciclo while para, si el usuario no ingresa 0 que es número para terminar, siga pidiendo que se ingrese número
    suma += numero   #A la variable suma se la utiliza como acumulador de los números ingresados
    numero = int(input("Ingrese un número: ")) #Se pide a usuario que ingrese número dentro de ciclo hasta que se ingrese un 0
    

print ("El resultado de la suma de los números ingresado es: ", suma) #Se imprimee por pantalla resultado



#Ejercicio5

#NO ESTOY SEGURO SI ES CORRECTO EL ALGORITMO, SI HACE LO QUE DEBE HACER. SIGO INVESTIGANDO


import random  #Se importa 
numeros_aleatorios = {random.randint(0, 9)}
intentos = 0

numero = int(input("Adivine! Ingrese un número "))

while numero != numeros_aleatorios:
    numero = int(input("Intentalo de nuevo. Ingrese un número"))
    
    intentos += 1

print ("Adivinaste! El número es: ", numeros_aleatorios, "Y lo adivinaste en ", intentos, " intentos")


#Ejercicio6

for numeros in range (100, -1, -1):  #Se utiliza ciclo for para que se puedan imprimer los números pares en forma decreciente entre 0 y 100
    print (numeros) #Se imprime resultado

#Ejercicio7

numero = int(input("Introduce un número entero positivo: ")) #Se solicita a usuario que ingrese un número positivo

suma = 0  #Se asigna a variable suma valor
for cont in range(0, numero + 1):  #Se utiliza ciclo for para que se sumen los números hasta llegar al valor del ingresado por usuario
        suma += cont  # Acumula la suma de cada número

print(f"La suma de todos los números desde 0 hasta {numero} es: {suma}")  #Se imprime por pantalla resultado

#Ejercicio8

par = 0 #Se asigna valor a variable
impar = 0  #Se asigna valor a variable
positivo = 0  #Se asigna valor a variable
negativo = 0   #Se asigna valor a variable
cant_numero = 100  #Se asigna valor a variable
suma = 0   #Se asigna valor a variable



for i in range(0, 100):  #Se utiliza ciclo for para iterar ingreso de números y acumularlos en las diferentes variables
    numeros = int(input(f"Ingrese un número {i + 1}: "))  #Se solicita a usuario que ingrese números
    
    if numeros %2 == 0: #Se compara número ingresado para saber si es par
        par += 1  #Se acumulan los números pares en variable par
    
    else:
        impar += 1  #En caso de que no sea par, se guarda y acumula los números ingresados impares en variable impar
   
    if numeros > 0:  #Se compara número ingresado para saber si es mayor a 0, positivo
        positivo += 1   #Se acumulan los números pares en variable positivo
    
    else:   
        negativo += 1   #En caso de que no sea positivo, se guarda y acumula los números ingresados menores de 0 en variable negativos

print (f"La cantidad de números pares es {par}")  #Se imprime por pantalla resultado
print (f"La cantidad de números impares es {impar}")  #Se imprime por pantalla resultado
print (f"La cantidad de números positivo es {positivo}")  #Se imprime por pantalla resultado
print (f"La cantidad de números negativo es {negativo}")  #Se imprime por pantalla resultado



#Ejercicio9

cant_numeros = 100  #Se asigna valor a variable
suma = 0  #Se asigna valor a variable

for contador in range (1, cant_numeros + 1): #se utiliza ciclo for para iterar cantidad de úmeros ingresados por usuario
    numero = int(input("Ingrese un numero "))  #Se solicita a usuario que ingrese números
    suma = suma + numero #Se acumula en variable suma, contador y acumulador, números ingresados
print ("La suma de los valores ingresados es ", suma)   #Se imprime por pantalla valor total de números ingresados
print ("El promedio de los números ingresados es ", suma / cant_numeros)  #Se imprime pr pantalla el promedio


#Ejercicio10

numero = input ("Ingrese un número ") #Se solicita que se ingrese un número

numero_invertido = numero [:: -1]  #Invertir el número    Utilizamos el operador de corte [::-1] para invertir la cadena.

print ("El número invertido es ", numero_invertido) #Muestra por pantalla el número invertido


