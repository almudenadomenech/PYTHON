

# Función sin parámetros
def saludar():
    print("Hola Mundo")
    
saludar() # llamada a la función
saludar()

# Función con un parámetro
def saluda2(nombre):
    print(f"¡Hola, {nombre}!")
    
saluda2("Almu")
saluda2("almu")

# Función con múltiples parámetros
def saludar3(nombre, hora_dia):
    print(f"Buenas  {hora_dia} {nombre}")
    
saludar3("Almu", "noches")
saludar3("Gema", "tardes")

# Funciones que devuelven un valor

def saludar4(nombre):
    return(f"Hola, {nombre}")

mensaje = saludar4("Luisa") #variable que almacena el valor devuelto por la función
print(mensaje) # llamada a la función

# Función que devuelve un valor, en este caso una suma
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print("Resultado:", resultado) # Imprimir el valor de la variable resultado

# Función para calcular el iva sobre el precio de un producto

def calcular_iva(precio_producto):
    iva = precio_producto * 0.21
    resultado_iva = precio_producto + iva
    print(f"precio final: {resultado_iva} €")
    return precio_producto + iva

calcular_iva (150)
calcular_iva (1250)

