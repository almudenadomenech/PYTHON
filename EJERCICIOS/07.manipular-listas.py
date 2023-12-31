nombres= ["almu", "Gema", "Susana", "Bea"]
print(nombres)

nombres[0]= "Almu"
print(nombres)

print(nombres[1:3])
print(nombres[0:])
print(nombres[:3])

# Mostra solo los pares
print(nombres[::2])

numeros = list(range(21))
print(numeros)
#numeros impares
print(numeros[1::2])

#Otra forma de sacar los numeros impares
numeros = list(range(1, 21))
print(numeros)
#numeros impares
print(numeros[::2])
