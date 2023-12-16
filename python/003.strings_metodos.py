
texto ='Hola curso Angular'

# Calcular la longuitud de un texto

longuitud= len(texto)
print ("Longuitud de texto", longuitud)

# Convertir a mayúsculas upper()

print(texto.upper())

## Crear una variable para guardar el texto en mayusculas
## y luego se imprime

texto_mayusculas = texto.upper()
print(texto_mayusculas)

# Convertir a minúsculas lower()

print(texto.lower())

# Partir un texto en base a un carácter split()
# Genera como resultado un lista de strings

palabras = texto.split() # Por defecto divide por espacios
print(palabras)   # ['Hola', 'curso', 'Angular']
print(len(palabras))  # Cuenta las palabras
print(palabras[0]) # Accede a la primera palabra
print(palabras[1]) # Accede a la segunda palabra
print(palabras[2]) # Accede a la tercera palabra
# print(palabras[3]) Da un error porque no existe la cuarta palabra

# Reemplazar texto dentro de un string, replace()
texto_python= texto.replace("Angular","Python") # Devuelve un nuevo string
print(texto_python)

# Extraer y convertir un número de una frase
precio_producto = "53.99 dolares"

# Paso 1: split
precio_elementos= precio_producto.split()
print(precio_elementos[0])

# Paso 2: Convertir texto a número float()
precio_num= float (precio_elementos[0])
print (precio_num)

# Paso 3: Sumar 5
precio_num= precio_num +5
print(precio_num)


descripcion_producto ="""
El producto textil {} tiene un precio de {} €.
"""
print(descripcion_producto.format("Abrigo lana", 100))
print(descripcion_producto.format("Guantes", 10))

