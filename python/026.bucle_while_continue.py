# Saltarnor el numero 5 en un conteo del 1 al 10
# Utilizamos continue

contador= 0

while contador < 10:
    contador += 1
    if contador == 5:
        continue
    print(contador)
    
#Imprimir los número impares entre 1 y 10

contador2 = 0
while contador2 < 10:
    contador2 += 1
    if contador2 % 2== 0:
        continue
    print(contador2)