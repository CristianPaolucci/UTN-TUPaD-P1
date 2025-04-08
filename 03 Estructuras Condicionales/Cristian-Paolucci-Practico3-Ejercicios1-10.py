#Ejercicio1

edad= int(input("Ingrese su edad"))  #Se solicita a usuario que ingrese su edad

MENOR_EDAD = 18  #Se asigna a constante valor 

if edad > MENOR_EDAD:   #Se compara el valor ingresado por usuario con constante y se toma desición
    print ("Es mayor de edad")  #Se imprime por pantalla resultado si es verdadero la condición
else:
    print ("Es menor de edad")    #Se impreme por pantalla si es falso la condición


#Ejercicio2

nota = float(input("Ingrese una nota"))  #Se pide a usuario que ingrese un valor

aprobado = 6  #Se asigna valor en caso aprobado
desaprobado = 5   #Se asigna valor en caso desaprobado

if nota >= aprobado:  #Se compara valor ingresado por usuario con variable y se toma decisión
    print ("Aprobado")  #Se imprime por pantalla resultado si es verdadero la condición
else:
    print ("Desaprobado") #Se imprime por pantalla resultado si es falsa la condición


#Ejercicio3

numero = int (input("Ingrese un número"))  #Se solicita a usuario que ingrese en valor

if numero % 2 == 0:   #Se compara valor ingresado para saber si es par o impar y se toma desición
    print ("Ha ingresado un número par")  #Se imprime por pantalla el resultado si es verdadero

else:
    print ("Por favor, ingrese número par")  #Se imprime por pantalla el resultado si es falso


#Ejercicio4

edad = int(input("Ingrese su edad"))  #Se solicita a usuario que ingrese su edad

NINIO = 11     #Se asigna valor a constante
ADOLESCENTE = 17  #Se asigna valor a constante
JOVEN = 29   #Se asigna valor a constante
ADULTO = 30   #Se asigna valor a constante

if edad < 0 or edad > 130:   #Se compara valor ingresado con rango de categoria
    print ("No pertenece a ninguna categoria")   #Se imprime por pantalla en caso falso, que no pertenezca a rango
elif edad <= NINIO:   #Se compara valor ingresado con constante y se toma decisión
    print ("Pertenece a la categoria Niño/a")    #Se imprime por pantalla resultado si es categoria niño
elif edad <= ADOLESCENTE:  #Se compara valor ingresado con constante y se toma decisión
    print ("Pertenece a la categoria Adolescente")   #Se imprime por pantalla resultado si es categoria adolescente
elif edad <= JOVEN:    #Se compara valor ingresado con constante y se toma decisión
    print ("Pertenece a la categoria Adulto/a joven")     #Se imprime por pantalla resultado si es categoria joven
else:
    print ("Pertenece a la categoria Adulto/a")   #Se imprime por pantalla resultado si es categoria adulto


#Ejercicio5

contrasenia = input("Ingrese un contraseña entre 8 y 14 caracteres: ")  #Se pide a usuario que que ingrese una contraseña

if 8 <= len (contrasenia) <= 14:  #Se compara si el valor ingresado por usuario tiene la cantidad correcta de caracteres utilzando función len()
    print ("Ha ingresado una contraseña correcta")  #Se imprime por pantalla que es correcta la cantidad de caracteres de la contaseña
else:
    print ("Por favor, ingrese una contraseña entre 8 y 14 caracteres")  #Se imprime por pantalla que el valor ingresado no contine la cantidad de caracteres correctos


#Ejercicio6

import random  #Se importa randon
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]  #se crea lista de 50 números entre 1 y 100 forma aleatoria
from statistics import mode, median, mean  #Importa paquete statistics, funciones para lista de números. Calcula moda, mediana, media de dichos números
print (mode, median, mean)  #Se imprime por pantalla moda, mediana, media

moda = mode (numeros_aleatorios)  #Se asigna a variable la moda de ciertos números aleatorios
mediana = median (numeros_aleatorios)  #Se asigna a variable la mediana de ciertos números aleatorios
media = mean (numeros_aleatorios)  #Se asigna a variable la media de ciertos números aleatorios

print (f"Lista de numeros aleatorios {numeros_aleatorios}")  #Se imprime por pantalla lista de números aleatorios
print (f"Moda {moda}")    #Se imprime por pantalla la moda de lista de números aleatorios
print (f"Mediana {mediana}")   #Se imprime por pantalla mediana de números aleatorios
print (f"Media {media}")    #Se imprime por pantalla media de números aleatorios

if media > mediana > moda:  #Se compara entre media, mediana, moda. Si media es mayor que mediana y mayor que moda el sesgo es positivo o a la derecha
    print ("Sesgo positivo o a la derecha")  #Se imprime por pantalla resultado. Tipo de sesgo
elif media < mediana < moda:   #Se compara entre media, mediana, moda. Si media es menor que mediana y menor que moda el sesgo es negativo o a la izquierda
    print ("Sesgo negativo o a la izquierda")   #Se imprime por panalla resultado. Tipo de sesgo
elif media == mediana == moda:   #Se compara entre media, mediana, moda. Si media es igual que mediana e igual que moda no contiene sesgo
    print ("Sin sesgo")    #Se imprime por panalla resultado. Tipo de sesgo
else:
    print ("El sesgo no se puede determinar de forma clara")   #Se imprime por pantalla en caso contario a lo anterior, que no se puede determinar


#Ejercicio7

frase = input ("Ingrese una palabra o frase: ")  #Se pide palabra o frase al usuario

if frase [-1].lower() in 'aeiou':  #Verifica si la ultimo caracter es vocal
    frase += "!"  #Se le agrega un signo de exclamación si termina en vocal

print (frase) #Se imprime por pantalla el resultado


#Ejercicio8

nombre = input("Ingrese su nombre: ")  #Se solicita a usuario que ingrese su nombre
opcion = int(input("Ingrese 1: nombre en MAYUSCULAS, Ingrese 2: nombre en minúsculas, Ingrese 3: nombre con primera Letra en mayúscula: "))  
                   #Se solicita a usuario que ingrese opción deseada
if opcion == 1:   #Se compara si el valor ingresado es 1
    opcion = nombre.upper()  #Se asigna a opción ingresada MAYUSCULAS con función upper()
elif opcion == 2:    #Se compara si el valor ingresado es 3
    opcion = nombre.lower()    #Se asigna a opción ingresada minúscula con función lower()
elif opcion == 3:     #Se compara si el valor ingresado es 3
    opcion = nombre.title()    #Se asigna a opción ingresada Primera Letra Mayúscula con función title()

print (opcion)  #Se imprime por panatlla opción elegida


#Ejercicio9

magnitud = int(input("Ingrese la magnitud del terremoto según la escala de Richter: "))  #Se solicita a usuario que ingrese una magnitud
 
if magnitud >= 1 and magnitud < 3:  #Se compara valor ingresado con rango
    print ("Muy leve (Imperceptible)")  #Se imprime por pantalla valor de rango elegido
elif magnitud >= 3 and magnitud < 4:    #Se compara valor ingresado con rango
    print ("Leve (Ligeramente perceptible)")   #Se imprime por pantalla valor de rango elegido
elif magnitud >= 4 and magnitud < 5:    #Se compara valor ingresado con rango
    print ("Moderado (Sentido por personas, pero generalmente no causa daños)")   #Se imprime por pantalla valor de rango elegido
elif magnitud >= 5 and magnitud < 6:     #Se compara valor ingresado con rango
    print ("Fuerte (Puede causar daños en estructuras débiles)")    #Se imprime por pantalla valor de rango elegido
elif magnitud >= 6 and magnitud < 7:     #Se compara valor ingresado con rango
    print ("Muy fuerte (Puede causar daños significativos)")   #Se imprime por pantalla valor de rango elegido
elif magnitud >= 7:    #Se compara valor ingresado con rango
    print ("Extremo (Puede causar graves daños a gran escala)")    #Se imprime por pantalla valor de rango elegido


#Ejercicio10

#NO HE PODIDO REALIZAR EL EJERCICIO EN FORMA CORRECTA. LO ENTREGO. SIGO BUSCANDO LA SOLUCION



hemisferio = input("Ingrese en cuál hemisferio se encuentra (N: Norte, S: Sur)").upper()
dia = int(input("Ingrese el día (1-31)"))
mes = int(input("Ingrese el mes (1-12)"))

h_norte = 'n'
h_sur = 's'

if (hemisferio == h_norte) and (((mes == 12 and dia >= 21 and dia <= 31) or (mes == 3 and dia >= 1 and dia <= 20)) or (mes == 1 and dia >= 1 and dia <= 31) or (mes == 2 and dia >= 1 and dia <= 29)):
    print ("Usted se encuentra invierno")

elif (hemisferio == h_sur) and (((mes == 12 and dia >= 21 and dia <= 31) or (mes == 3 and dia >= 1 and dia <= 20)) or (mes == 1 and dia >= 1 and dia <= 31) or (mes == 2 and dia >= 1 and dia <= 29)):
    print ("Usted se encuentra verano")

elif (hemisferio == h_norte) and (((mes == 3 and dia >= 21 and dia <= 31) or (mes == 6 and dia >= 1 and dia <= 20)) or (mes == 4 and dia >= 1 and dia <= 30) or (mes == 5 and dia >= 1 and dia <= 31 )):
    print ("Usted se encuentra en primavera")

elif (hemisferio == h_sur) and (((mes == 3 and dia >= 21 and dia <= 31) or (mes == 6 and dia >= 1 and dia <= 20)) or (mes == 4 and dia >= 1 and dia <= 30) or (mes == 5 and dia >= 1 and dia <= 31 )):
    print ("Usted se encuentra en otoño")

elif (hemisferio == h_norte) and (((mes == 6 and dia >= 21 and dia <= 30) or (mes == 9 and dia >= 1 and dia <= 20)) or (mes == 7 and dia >= 1 and dia <= 31) or (mes == 8 and dia >= 1 and dia <= 31 )):
    print ("Usted se encuentra en verano")

elif (hemisferio == h_sur) and (((mes == 6 and dia >= 21 and dia <= 30) or (mes == 9 and dia >= 1 and dia <= 20)) or (mes == 7 and dia >= 1 and dia <= 31) or (mes == 8 and dia >= 1 and dia <= 31 )):
    print ("Usted se encuentra en invierno")

elif (hemisferio == h_norte) and (((mes == 9 and dia >= 21 and dia <= 30) or (mes == 12 and dia >= 1 and dia <= 20)) or (mes == 10 and dia >= 1 and dia <= 31) or (mes == 11 and dia >= 1 and dia <= 30 )):
    print ("Usted se encuentra en otoño")

elif (hemisferio == h_norte) and (((mes == 9 and dia >= 21 and dia <= 30) or (mes == 12 and dia >= 1 and dia <= 20)) or (mes == 10 and dia >= 1 and dia <= 31) or (mes == 11 and dia >= 1 and dia <= 30 )):
    print ("Usted se encuentra en primavera")


#Ejercicio10Bis

#NO HE PODIDO REALIZAR EL EJERCICIO EN FORMA CORRECTA. LO ENTREGO. SIGO BUSCANDO LA SOLUCION




def obtener_estacion(hemisferio, mes, dia):
    estaciones_norte = {
        (12, 21, 3, 20): "Invierno",
        (3, 21, 6, 20): "Primavera",
        (6, 21, 9, 20): "Verano",
        (9, 21, 12, 20): "Otoño",

    }

    estaciones_sur = {
        (12, 21, 3, 20): "Verano",
        (3, 21, 6, 20): "Otoño",
        (6, 21, 9, 20): "Invierno",
        (9, 21, 12, 20): "Primavera",

    }

    if hemisferio == 'n':
        obtener_estacion == estaciones_norte
    elif hemisferio == 's':
        obtener_estacion == estaciones_sur



hemisferio = input("Ingrese el hemisferio dónde se encuentra (Norte:'n'/Sur:'s'): ")
mes = int(input("Ingrese el mes (1-12)"))
dia = int(input("Ingrese el día (1-31)"))

norte = 'n'
sur = 's'

estacion = obtener_estacion(hemisferio, dia, mes)

print (f"La estación en el hemisferio {'norte' if hemisferio == 'n' else 'sur'} es: {estacion}")

