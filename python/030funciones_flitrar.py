def filtrar_precio1(precios): # Solo filtra los precios
    for precio in precios:
        print(precio)
        
precios = [20.99, 53.22, 32.77, 55.00, 300.12]
filtrar_precio1(precios)

def filtrar_precio2(precios, precio_min, precio_max): # filtra precios
    for precio in precios:
        if precio_min < precio < precio_max:
            print(precio)

precios = [20.99, 53.22, 32.77, 55.00, 300.12]
filtrar_precio2(precios, 30, 60)



def filtrar_precio3(precios, precio_min, precio_max):

    ## for que itere sobre la lista de precios
        # filtrar si el precio esta entre min y max
        # guardar el precio en una lista de precios
    precios_filtrados = []
   
    for precio in precios:
        if precio_min < precio < precio_max:
            precios_filtrados.append(precio)
    return precios_filtrados

precios=[10.99, 99.56, 53.23,120.76, 32.44]
precios_filtrados = filtrar_precio3(precios, 5, 55)
print(precios_filtrados)
print( filtrar_precio3(precios, 20, 100))