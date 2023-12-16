
nombre = input ('Por favor introduce tu nombre:')
print ("El nombre es:", nombre)

edad = input ('Introduce edad')
print("Edad es:", edad)

edad_num = int (edad) # Convierte de texto a número int
print (edad_num + 1) # pobamos una operación aritmética cualquiera


# leer peso con decimales float()
peso= input ('Introduce tu peso: ')
peso_num = float (peso)
print(peso_num - 5)

# Leer si está de alta True o False no bool()
print(bool()) # False
print(bool(1)) # True
print(bool(0)) # Falso
print(bool("")) # Texto vacio False
print(bool("Hola")) # Texto con contenido True
emails= ['u1@gmail.com', 'u2@gamail.com']
print(bool(emails)) # la lista tiene elementos, True
mensajes= [] # La lista esta vacia
print(bool(mensajes)) # False

alta= input('Introduce si esdado de alta (1 o 0)')
alta_bool= bool (int(alta)) # Int para hcerlo de tipo entero
print('Esta dado de alta', alta_bool)

alta_bool =input('Introduce si está dado de alta 1 o 0') == '1' # True o False
print('Esta dado de alta', alta_bool)