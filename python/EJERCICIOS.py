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