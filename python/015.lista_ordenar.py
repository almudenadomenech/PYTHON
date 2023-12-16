
# Ordenar elementos .sort() por defecto de manera ascendente

coches =['Mercedes Clase A','BMW 320', 'Audi A5', 'Skoda']
coches.sort()
print(coches)
 

precios = [23.50, 58.25, 14.64, 58.54, 587.58]
precios.sort()
print(precios)

# sort(reverse=True) o reverse() ordena de manera descendente
coches.reverse()
print(coches)

precios.reverse()
print(precios)
precio_maximo = precios[0] # Al estar odenado de más a menos el primero es el más alto
precio_minimo = precios[-1]
print(f"El precio máximo es: {precio_maximo}")
print(f"El precio mínimo es: {precio_minimo}")