def suma(a, b):
    print( a+ b)
    

suma(2, 6)


def suma(*numeros):
    resultado= 0
    for numero in numeros:
        resultado += numero
    print(resultado)
                
suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)


def multiplicar (*numeros):
    resultado= 1
    for numero in numeros:
        resultado *= numero
    print(resultado)

multiplicar(3, 4)
multiplicar(3, 5, 16)