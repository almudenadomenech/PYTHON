a= 10
print(type(a))
print(a)

nombre = 'Almudena'
print(nombre)
nombre1 = str('Domenech')
print(nombre1)

edad = 18
print(edad + 1)

texto = 'Hola estamos en el curso de Python'
print(len(texto))
print(texto.upper())
print(texto.lower())

texto2 = 'Adios acabamos de terminar el curso'
print(len(texto2))
print(texto2.upper())
print(texto2.lower())

texto3 = 'Acabamos de empezar el curso de Python'
print(len(texto3))
print(texto3.upper())
print(texto3.lower())

cadena= 'Hola me llamo Almudena Domenech'
print(len(cadena))
print(cadena.upper())
print(cadena.lower())

palabras = cadena.split()
print(palabras)

palabras1 = texto3.split()
print(palabras1)

print(len(palabras))
print(palabras[0])
print(palabras[1])

print(cadena[0])

reemplazar = cadena.replace('Hola', 'Adios')
print(reemplazar)
num = 5
num1 = 3
suma = num + num1
print(suma)
precio = suma * 3
print(precio)


descripcion = """
El producto textil {} tiene un precio de {} €"""
print(descripcion.format("abrigo", 150))
print(descripcion.format('Guantes', 25))

nombre= input("Introduce tu nombre: ")


apellido = input('Introduce tu apellido: ')


nombre_completo = nombre + apellido
print('Tu nombre completo es:' ,nombre_completo)

edad = input('Introduce tu edad:')
print('Tu edad es:', edad)
edad_num = int(edad)
print(edad_num + 1)

peso = input('Introduce tu peso:')
print('Tu peso es:', peso)
peso_total = float(peso)
print(peso_total -4.6)
print(type(peso_total))


print(30/50)
print(round(30 /35, 2))

print(50 // 35)

caramelos = 50
alumnos = 17
reparticion = caramelos // alumnos
print(f"Cada alumno recibira {reparticion} caramelos.")

mesas= 50
camareros = 3
total = mesas // camareros
print(f"Cada camarero atenderá {total} mesas")

print("hola" == "hola")
print("Hola" == "Ola")

edad = int(input('Intrudice tu edad: '))
print(edad == 18)

nombre= str(input('Introduce tu nombre:'))
print(nombre == "Almudena")

password = '1234'
input_password = input('Introduce tu contraseña:')
print(input(input_password == password))
print(input(input_password != password))

if password != input_password:
    print('Contraseña incorrecta')
    
    
respuesta_correcta = 'madrid'

respuesta_usuario = input('Cual es la capital de España:').lower()
if respuesta_usuario != respuesta_correcta:
    print('Resultado incorrecto')
else:
    print('Respuesta correcta')
    
    
usuario_correcto = 'admin'
password_correcta = '1234'

usuario = input('Introduzca usuario:')
password = input('Introduzca contraseña:')

if usuario == usuario_correcto and password == password_correcta:
    print('credenciales correctas')
else:
    print('Credenciales incorrectas')
    
es_estudiante = input('¿Es estudiante? (si/no):').lower() == 'si'
precio_total = float(input('Introduce precio de compra: '))
if es_estudiante or precio_total > 100:
    precio_total = round(precio_total * 0.80, 2)
    print(f'Tienes un descuento, precio :{precio_total}')
else:
    print(f'No tienes descuento, precio: {precio_total}')
    
    
edad_usuario = int(input('Introduce tu edad: '))

if not edad_usuario >= 18:
    print('No tiene acceso')
else:
    print('Tiene acceso')



a = 20
b = 10
print (a is not b)

lista = [1, 2, 3, 4, 5, 6]
print (1 in lista)

numero = 10
if numero > 5:
    print("el numero es mayor a 5")
    
    
ropa = ['camisa', 'pantalon', 'falda', 'vestido']
print(ropa)

ropa.append('bufanda')
print(ropa)

ropa.append('guantes')
print(ropa)

ropa.insert(0, 'camiseta')
print(ropa)

ropa.remove('camiseta')
print(ropa)

print(len(ropa))
ropa.sort()
print(ropa)

ropa.reverse()
print(ropa)

hora = int(input('Introduce una hora:'))
if hora <8:
    print('Estoy durmiendo')
elif hora >=8 and hora <= 14:
    print('Estoy en clase')
elif hora >14 and hora <=15:
    print('Estoy comiendo')
else:
    print('Estoy descansando')
    
    
contador = 0
while contador < 10:
    contador += 1
    print(f'contador: {contador}')


password_correct = 'admin'
password = ""
while password != password_correct:
    password = input('Introduce la password: ').replace("", "")
print('Credenciales correctas')

numeros = [1, 2, 3, 4]
for n in numeros:
    print('Hola Almudena.')
    
coleccion = [5, 10, 'Python', 20]
for i in coleccion:
    print(f"Elento: {i}")
    
for i in range(5):
    print('Hola')
    
    
lista = [1, 2, 3, 4, 5]
suma = 0
for num in lista:
    suma += num
print('La suma es:', suma)

words = ["Son", "las", "10:45 am"]
sentence = ""
for w in words:
    sentence +=w + " "

print("Frase:", sentence)

# Crear una lista de número del 1 al 5

numeros = [1, 2, 3, 4, 5]
for num in numeros :
    if num == 3:
        break
    print(num)
    
    
print('Hola Mundo')
saludo= 'Hola Mundo'
print(saludo)

nombre = input('Introduce tu nombre: ')
print('Hola' + nombre)

nombre = input ('¿Cómo te llamas? ')
n = input ('Introduce un numero entero: ')
print((nombre + '\n')* int(n))


contador = 0

while contador < 10:
    contador += 1
    print(f'contador: {contador}')
    
contador = 0

while contador <5:
    contador += 1
    print(contador)
    
    
    
def saludo(nombre='Amigo'):
    print("Hola, " + nombre +". ¡Buen día!")
    
saludo('Almu')
print(saludo)
    
    
def cuadrado(numero):
    return numero **2

resultado = cuadrado(4)
print(resultado)


def calculate_iva(product_price):
    product_iva = product_price * 0.21
    result = product_price + product_iva
    print("Precio final producto: " + str(result) + "€")
    return result


calculate_iva(50)
print(calculate_iva)

def hola():
    print('Estamos dentro de la función hola')
    if 5 == 5:
        print('Adios')
    if 4 < 5:
        print('hola')
        
hola()
print(hola)


def multiplicar(num1, num2):
    
    return num1 * num2


resultado= multiplicar(5, 3)
print(resultado)



    
    

