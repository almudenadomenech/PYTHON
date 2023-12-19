


def sumatorio(numeros):
    """Calcula el sumatorio y lo devuelve
    Args:
        numeros(lista): lista de números int o float
    """
    #pass ( se pone cuando no hay codigo)
    sumatorio = 0

    
    for num in numeros:
       sumatorio += num
    return sumatorio

    
## Al utilizar la función vscode muestra su docstring
## INVOCAR LA FUNCION
## PRIMERO CREAMOS LA LISTA
numeros =[1, 2, 3, 4, 5]
resultado = sumatorio(numeros) # El resultado de la función sumatorio lo guardo en una variable
print('la suma es:', resultado)
resultado2 = sumatorio([100, 200, 300])
