# Bucle for con break
# Nos permite salir completamente del bucle for cuando se cumpla 
# una condición específica

# Crear lista de números del 1 al 5
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    if num == 3:
        break
    print(num)
    
# Buscar una fruta en específico de una lista de frutas
frutas= ["manzana","pera","melon","naranja", "cereza", "sandia"]
for fruta in frutas:
    if fruta == "cereza":
        print("cereza encontrada")
        break
    print(f"Revisando {fruta}...")
    
# Un bucle utilizando la función range() que tenga un break
for i in range(10):
    if i == 4:
        break
    print(i)
    
# Bucle for que se interrumpa (break) cuando se encuentre una letra
# en una cadena de texto (string)
# crear una variable que sea de tipo string

vocales= "aeiou"
for vocal in vocales:
    if vocal == "i":
        print("vocal encontrada")
        break
    print(vocal)
    
