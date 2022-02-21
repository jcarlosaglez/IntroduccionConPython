# program.py
# 1.- Programa en python
sum = 1+2
print(sum)

# 2.- Ejecución Python nombreArchivo.py

# 3.- Función print()
print('Hola desde la consola')

# 4.-Variables
sum = 1 + 2 # 3
product = sum * 2
print(product)

# 5.- Tipos de datos
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

# 6.- Se puede saber su tipo al verlos o al ejecutar la función type()
# Declaramos la variable
distancia_a_alfa_centauri = 4.367

# Descubrimos su tipo de dato
print(type(distancia_a_alfa_centauri))

# 7.- Operadores <left side> <operator> <right side>
left_side = 10
right_side = 5
left_side / right_side # 2

# Aritméticos +, -, *, /
#Asignación =, +=, -=, /=, *=

# 8 Fechas - Se necesita del modulo date -> 'from datetime import date'
from datetime import date
print(date.today())

# 9 Conversión de tipos
#Error -> print("Today's date is: " + date.today())
print('Today´s date is: ' + str(date.today()))

# 10 Recopilar información
#Entrada de usuario con metodo input()
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

#Entrada de números, el método input solo almacena cadenas
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(first_number + second_number)
#Para que el programa responda bien se debe cambiar el tipo
print(int(first_number) + int(second_number))