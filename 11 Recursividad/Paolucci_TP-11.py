#Ejercicio1

#definicion de función
def factorial (num):
    if num == 0:
        return 1
    else:
        return num * factorial (num - 1)

#Programa Principal

numero = int(input("Ingrese un numero"))
print (factorial(numero))

#Ejercicio2

#Se define la funcion

def fibonacci (posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)
    
 #Programa principal

posicion = int(input("Ingrese la psoicion que desea ver la serie Fibonacci "))

print (fibonacci(posicion))

#Ejercicio3

#Se definen funciones

def potencia (n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)
    
def main():
    base = int(input("Ingrese la base "))
    exponente = int(input("Ingrese el exponente "))

    resultado = potencia(base, exponente)
    print (f"{base}^{exponente} = {resultado}")

#Ejecutar programa

main ()

#Ejercicio4

#Se define funciones
def decimal_a_binario (n):
    if n == 0:
        return ''
    else:
        return decimal_a_binario (n // 2) + str(n % 2)
    
def main ():
    numero = int(input("Ingrese un numero "))
    if numero == 0:
        print ("El numero binario es 0")
    else:
        binario = decimal_a_binario(numero)
        print (f"El numero {numero} en binario es {binario}")

#Programa Principal
main ()


#Ejercicio5

#Definicion de funcion
def es_palindromo(palabra):
    if len (palabra) <= 1:
        return True
    if palabra [0] != palabra [-1]:
        return False
    return es_palindromo (palabra[1 : -1])

#Programa Principal
entrada_palabra = input("Ingrese la palabra ").lower()
if es_palindromo(entrada_palabra):
    print ("La palabra ingresada es un palindromo")
else:
    print("La palabra ingresada no es un palindromo")


#Ejercicio6

def suma_digitos (num):
    if num < 10:
        return num
    else:
        return num % 10 + suma_digitos(num // 10)
    
numero = int (input("Ingrese un numero"))
resultado = suma_digitos(numero)
print (f"La suma de los digitos de {numero} es {resultado}") 

#Ejercicio7

def contar_bloques (n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
print (contar_bloques(5))


#Ejercicio8

def contar_digito (numero, digito):
    if numero == 0:
        return 0
    coincide = 1 if numero % 10 == digito else 0
    return coincide + contar_digito (numero // 10, digito)

print (contar_digito (28883888, 8))
