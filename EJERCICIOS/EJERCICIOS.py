texto= "Hola"
print(texto)

a= 1
b= 2
suma= a + b
print(suma)
print('La suma es:', suma)

texto = 'Hola me llamo Almudena'
longuitud = len(texto)
print(longuitud)

texto1= 'a, b, c, d, e'
longuitud1= len(texto1)
print('la longuitd del texto es:',longuitud1)
texto_mayusculas= texto1.upper()
print('el texto en mayusculas:', texto_mayusculas)

texto_mayusculas1= texto.upper()
print('eltexto en mayusculas:', texto_mayusculas1)

frase= 'Buenos días, mi nombre es Almudena'
longuitud = len(frase)
print('la longuitud es:',longuitud)
mayusculas= frase.upper()
print('En mayusculas:', mayusculas)

FRASE= 'BUENOS DIAS, MI NOMBRE ES ALMU'
longuitud2= len(FRASE)
print('la longuitud de la frase es:', longuitud2)

print('En minúsculas:', FRASE.lower())
print('En mayusculas', FRASE.upper())

texto_2= 'la casa es bonita'
print('Texto en mayusculas',texto_2.upper())

texto3= 'ME VOY DE VACACIONES'
print('En minusculas:', texto3.lower())

palabras = texto.split()
print(palabras)
print(palabras[0])
print(palabras[1])

texto_adios = texto.replace('Hola', 'Adios')
print(texto_adios)

text_fea = texto_2.replace('bonita', 'fea')
print(text_fea)

descripcion = ''' el producto {} tiene un precio de:{}€'''
print(descripcion.format('Abrigo', 100))
print(descripcion.format('Guantes', 25))

nombre = input('Introduce tu nombre:')
apellido = input(' Introduce tu apellido:')
nombre_completo = nombre + " " + apellido
print('Tu nombre completo es:', nombre_completo)
longuitud3= len(nombre_completo)
print('La longuitud es:', longuitud3)
mayusculas= nombre_completo.upper()
print('Nombre completo en mayusculas:', mayusculas)
minusculas= nombre_completo.lower()
print('Nombre completo en minusculas:',minusculas)

precio= input('Introduce un precio: ')
precio_num= float(precio)
print('el precio es:', precio_num)

sueldo= input('Introduce tu sueldo:')
sueldo_num= float(sueldo)
print('Tu sueldo es:', sueldo_num)

respuesta= input('Intruduce (s/n):')
respuesta_bool= bool(str(respuesta))
print('la respuesta es:', respuesta_bool)

print(type("Hola"))

print( 25/5)
print( 5+5)
print(25//5)
print(150/45)
print(round(150/45, 2))
print(round(1580/47, 2))

libros= 18
personas= 5
division= libros//personas
print(division)

print(f'cada persona tendra: {division} libros')

password= "1234"

respuesta= input('Introduce password:')
if respuesta == password:
    print('password correcta')
else:
    print('Vuelve a intentarlo')
    

respuesta= "Madrid"
Acierto = input('Cual es la capital de España?:').lower
if Acierto== respuesta:
    print('Respuesta correcta')
    
    
    
usuario_correcto= 'admin'
password_correcta= '1234'

usuario= input('Introduce tu usuario:')
password= input ('Introduce tu password:')

if usuario_correcto == usuario and password_correcta == password:
    print('Credenciales correctas')
else:
    print('Credenciales incorrectas')
    
es_estudiante = input('¿Es estudiante? (si/no): ').lower()== 'si'
precio_total = float(input('Introduce compra: '))

if es_estudiante or precio_total > 100:
    precio_total = round(precio_total * 0.80, 2)
    print(f'Tienes descuento, precio: {precio_total}')
else:
    print(f'No tienes descuento: {precio_total}')
    
print("A" in 'Almudena')

lista1 = ['almu', 'maria', 'carmen', 'juan', 'pedro']
print(lista1)
del lista1 [1]
print(lista1)

lista1 = ['almu', 'maria', 'carmen', 'juan', 'pedro']
print(lista1)
lista1.remove('almu')
print(lista1)

contador = 0
while contador < 10:
    contador += 1
    print(f'contador: {contador}')
    
    
password_correct = "admin"
password = ""

while password != password_correct:
    password = input('Introduce la password: ').replace(" ", "")
    
print('Credenciales correctas.')


estaciones = ['verano', 'invierno', 'otoño', 'primavera']
estacion= ''
while estacion not in estaciones:
    estacion = input('Introduce estacion: ')
    
print ('estacion correcta')

a= 10
b = 5
print( a + b)
print( a - b)
print(a * b)
print(a / b)
print (a % b)
print (a ** b)
print( a // b)

c= 7
d = 4
print(c == d)
print(c != d)
print(c > d)
print(c < d)
print(c >= d)
print(c <= d)

c += 3
c -= 3
c *= 3
c /= 3
c %= 3
c **= 3
c //= 3

t= True
f= False

print( t and f)
print(t or f)
print( not f)

num1= 10
num2 = 10
print( num1 is num2)
print(num1 is not num2)

lista = [1, 2, 3, 4, 5]
print(2 in lista)
print(8 not in lista)

# EJERCICIO CERTIDEVS

num = 4
if num > 0:
    print('el numero es positivo')
elif num ==0:
    print('el numero es igual a 0')
else:
    print('el numero es negativo')
    
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    print(numero)
    
    
num1= 1    
while num1<= 10:
    print(num1)
    num1+=1
    
numeros= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero == 5:
        break
    print(numero)
    
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero == 5:
        continue
    print(numero)
    

  
entero = 1
flotante = 1.50
complejo = 2 + 3j
booleano = True
texto= 'Hola mundo'


palabra='murcielago'
letra1= palabra[0]
print(letra1)
letra9= palabra[9]
print(letra9)
  
    
def multiplicar(num1, num2, num3=4):
    return num1 * num2

resultado = multiplicar(3, 5)
print(resultado)


def multiplicar(num1, num2, num3= 4):
    """Esta funcion multiplica """
    return num1 * num2
resultado = multiplicar(5, 3)
print(resultado)

def saludar(nombre='Amigo'):
    """Esta funcion imprime un saludo"""
    print("Hola, " + nombre +"Buen día")


def es_par(numero):
    """Esta función define si un numero es par o impar"""
    if numero //2:
        return True
    else:
        return False
    

resultado= es_par(2)
print(resultado)   





def multiplicar(num1, num2):
    """Esta función multiplica dos parámetros"""
    return num1 * num2

resultado= multiplicar(5, 3)
print(resultado)

def multiplicar(num1, num2, num3= 1):
    """El tercer parámetro es opcional"""
    return num1 * num2 * num3


resultado= multiplicar(5, 3)
print(resultado)

def saludar(nombre= 'Amigo'):
    """Esta función imprime un saludo"""
    print("Hola, "+ nombre + " " +"Buen día")

saludar('Almu')
print(saludar)


def es_par(numero):
    """Esta función define si un numero es par o impar"""
    if numero %2 == 0:
        return True
    else:
        return False
    

resultado= es_par(1)
print(resultado)     

try:  
    print(x)
except:
    print("An exception occurred")
print("Hola")


    



 

