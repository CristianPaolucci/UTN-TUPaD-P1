#Ejercicio1

def imprimir_hola_mundo():     #Se define la función
     print("Hola mundo")        #Instrucción que se ejecuta cuando llame a la función

#Programa principal

imprimir_hola_mundo()         #Llama la  funcion


#Ejercicio2

def saludar_usuario(nombre):   #Se define función y recibe un nombre
    return f"Hola {nombre}"    #Lo que devuelve la función, saludo concatenado con nombre


#Programa principal

nombre_usuario = input("Ingrese su nombre ")  #Se solicita a usuario que ingrese un nombre
saludar = saludar_usuario(nombre_usuario)   #Se llama a la función con ese nombre y se guarda resultado en saludar
print(saludar)  #Se imprime el saludo


#Ejercicio3

def informacion_personal(nombre, apellido, edad, residencia):  #Se define función y recibe por parámetro nombre, apellido, edad, residencia
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"  #Lo que devuelve la función, concatenando los parámetros recibidos


#Programa principal

nombre_usuario = input("Ingrese su nombre ")  #Se solicita a usuario que ingrese su nombre
apellido_usuario = input("Ingrese su apellido ")    #Se solicita a usuario que ingrese su apellido
edad_usuario = int(input("Ingrese su edad "))     #Se solicita a usuario que ingrese su edad
residencia_usuario = input("Ingrese su residencia ")     #Se solicita a usuario que ingrese su residencia

datos_personales = informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)  #Se llama a la función,se envían los argumentos y se guarda en variable
print (datos_personales)  #Se imprime Los datos personales


#Ejercicio4

def calcular_area_circulo(radio):  #Se define la función y recibe por parámetro el radio
    import math    #Se importa modulo math de librería de python
    area = math.pi * (radio ** 2)  #Se calcula el área utilizando constante pi
    return area  #Devuelve resultado del cálculo del área


def calcular_perimetro_circulo(radio):    #Se define la función y recibe por parámetro el radio
    import math    #Se importa modulo math de librería de python
    perimetro = 2 * math.pi * radio    #Se calcula el perímetro utilizando constante pi
    return perimetro     #Devuelve resultado del cálculo del perímetro



#Programa principal

radio_circulo = float (input("Ingrese el radio del círculo "))  #Se solicita a usuario que ingrese el radio del círculo
resultado_area_circulo = calcular_area_circulo(radio_circulo)  #Se llama a la función,se envían los argumentos y se guarda en variable
resultado_perimetro_circulo = calcular_perimetro_circulo(radio_circulo)    #Se llama a la función,se envían los argumentos y se guarda en variable

print (f"El área del circulo es {resultado_area_circulo}")  #Se imprime resultado
print (f"El perímetro del circulo es {resultado_perimetro_circulo}")   #Se imprime resultado


#Ejercicio5

def segundos_a_horas(segundos):  #Se define la función y se recibe por parámetro los segundos
    horas = segundos / 3600     #Se realiza el calculo para saber equivalente segundos a horas
    return f"La cantidad de segundos ingresados equivale a {horas} horas"  #Devuelve resultado concatenado con texto


#Programa principal

segundos_ingresados = int(input("Ingrese la cantidad de segundos a transformar "))  #Se solicita a usuario que ingrese los segundos
resultado_segundos_a_horas = segundos_a_horas(segundos_ingresados)    #Se llama a la función,se envían los argumentos y se guarda en variable
print (resultado_segundos_a_horas) #Se imprime resultado



#Ejercicio6

def tabla_multiplicar(numero):  #Se define función y se recibe por parámetro número
    print (f"La tabla de multiplicar del {numero}: ")  #Imprime texto concatenado con lo que contiene variable numero
    for i in range(1, 11):  #Se utiliza ciclo for para contar rango desde dónde comienza hasta dónde termina
        multiplicador = numero * i  #Variable donde se guardan los resultados de operación, se utiliza como contador y acumulador
        print (f"{numero} * {i} = {multiplicador}")  #Imprime tabla de multiplicar


#Programa principal

numero_a_multiplicar = int(input("Ingrese un número para calcular en la tabla de multiplicar "))  #Se solicita a usuario que ingrese el número que desea para tabla
resultado_numero_a_multiplicar = tabla_multiplicar(numero_a_multiplicar)  #Se llama a la función,se envían los argumentos y se guarda en variable



#Ejercicio7

def operaciones_basicas(a, b): #Se define función y recibe por parámetro lo que contiene variable a y b
    suma = a + b  #Se realiza la suma y se guarda en variable
    resta = a - b   #Se realiza la resta y se guarda en variable
    multiplicacion = a * b   #Se realiza la multiplicación y se guarda en variable
    
    if b != 0:   #Se verifica si b es distinto de 0 para evitar división por cero
        division = a / b  #Se realiza división si b es distinto a cero
    else:  #En caso de que b sea igual a cero
        print ("No se puede dividir por cero")  #Se imprime imposibilidad de poder dividir
    return (suma, resta, multiplicacion, division)  #Se devuelve resultado de operaciones

# Programa principal

a = float(input("Ingresa el primer número: "))  #Se solicita a usuario que ingrese un número
b = float(input("Ingresa el segundo número: "))   #Se solicita a usuario que ingrese un número

resultados = operaciones_basicas(a, b)   #Se llama a la función,se envían los argumentos y se guarda en variable

print("\nResultados de las operaciones básicas:")
print(f"Suma: {resultados[0]}")  #Se imprime resultados
print(f"Resta: {resultados[1]}")   #Se imprime resultados
print(f"Multiplicación: {resultados[2]}")    #Se imprime resultados
print(f"División: {resultados[3]}")   #Se imprime resultados
    

#Ejercicio8

def calcular_imc(peso, altura):   #Se define función y se recibe por parámetro peso y altura
    imc = peso / altura ** 2   #Se calcula el índice de masa corporal y se guarda en variable
    return imc  #Se devuelve el resultado

#Programa principal

peso_usuario = float(input("Ingrese su peso"))   #Se solicita a usuario que ingrese su peso y se guarda en variable
altura_usuario = float(input("Ingrese su altura"))   #Se solicita a usuario que ingrese su altura y se guarda en variable
resultado_peso_altura = calcular_imc(peso_usuario, altura_usuario)  #Se llama a la función,se envían los argumentos y se guarda en variable
print (f"Su indice de masa corporal es {resultado_peso_altura: .2f}")  #Se imprime resultado concatenando texto con lo que contiene variable y se formatea
                                                                       #el reultado para que solo muestre dos cifras decima


#Ejercicio9

def celsius_a_fahrenheit(celsius):  #Se define función y se recibe por parámetro valor de grados celsius
    conversor_fahrenheit = (celsius * 9/5) + 32  #Se calcula y convierte de celsius a fahrenheit
    return conversor_fahrenheit   #Se devuelve resultado convertido


#Programa principal

celsius = float(input("Ingrese la cantidad de grados celsius que desea convertir a grados fahrenheit "))  #Se solicita a usuario que ingrese los grados celsius a convertir
resultado_fahrenheit = celsius_a_fahrenheit(celsius)  #Se llama a la función,se envían los argumentos y se guarda en variable

print(f"El equivalente a {celsius}°C ingresados a fahrenheit es {resultado_fahrenheit}°F")  #Se imprime resultado concatenando los grados ingresados con los grados convertidos


#Ejercicio10

def calcular_promedio(a, b, c):  #Se define función y se recibe por parámetro lo que contiene los argumentos a, b, c
    promedio = (a + b + c) / 3  #Se realiza calculo de promedio y se guarda en variable
    return promedio  #Se devuelve resultado


#Programa principal

num1 = float(input("Ingrese el primer número a calcular "))  #Se solicita a usuario que ingrese un número
num2 = float(input("Ingrese el segundo número a calcular "))   #Se solicita a usuario que ingrese un número
num3 = float(input("Ingrese el tercer número a calcular "))    #Se solicita a usuario que ingrese un número
resultado_promedio = calcular_promedio(num1, num2, num3)     #Se llama a la función,se envían los argumentos y se guarda en variable

print (f"El promedio de los números ingresados es {resultado_promedio: .2f}")  #Se imprime resultado concatenando texto con lo que contiene variable y se formatea
                                                                       #el reultado para que solo muestre dos cifras decimales
