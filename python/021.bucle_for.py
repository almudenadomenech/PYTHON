
# Bucle For

# Se puede utilizar con diferentes colecciones de datos (lista, diccionarios, conjuntos, etc)
# Es una estructura iterativa(repetir un proceso un número determinado de veces)
# Bucle con un número determinado de iteraciones

for i in [1, 2, 3, 4, 5]:
    print("Hola mundo")
    
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print("Hola Mundo")
    
# Una lista puede contener elementos de diferentes tipos
# No tienen que ir ordenados
# Esta iterando sobre la cantidad de elementos de la lista, no sobre el tipo de dato, 
# no asigna un valor a cada elemento

for i in [1, 10, 3, "Almu"]: # Contar los elementos de la lista, no el tipo de dato, son 4 elementos
    print("Ejercicio bucle for")

coleccion= [5, 10, "python", 20]
for i in coleccion:
    print(f"Elemento:{i}")
    
# Iterar sobre una lista de frutas

frutas= ["manzana", "pera", "platano","melon"]
for i in frutas:
    print(f"frutas:{i}")
    
# Utilizar la función "range()" para generar una lista de numeros
for i in range(5):
    print(i)
    
# Imprimir "HOLA" 5 veces
for i in range(5):
    print("HOLA")
    
# Iterar sobre una cadena de texto
palabra= "Descando"
for i in palabra:
    print(i)

frase= "Descando a las 11" # Iterar sobre cada caracter, incluyendo los espacios
for i in frase:
    print(i)
    
# Iterar sobre cadena de texto pero sin salto de línea
nombre= "Almu"
for i in nombre:
    print(f"{i}", end="")
    
# Sumar los elementos de una lista
numeros= [1, 2, 3, 4, 5]
# Crear variable acumuladorea
suma = 0 # inicializar en 0
for num in numeros:
    suma += num # en cada iteración, el valor de num se suma al valor actual de la suma
print("La suma es:",suma)

# Concatenar cadenas de texto de una lista
words = ["Son", "las", "10:45 am"]
sentence = ""

for w in words:
    sentence += w + " "
print("Frase:", sentence)

