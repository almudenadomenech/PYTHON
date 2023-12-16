
# Sistema de puntuación

puntos = int(input('Introduce puntos: '))
nivel = int(input('Introduce nivel:'))

if nivel == 1:
    if puntos < 20:
        print('Tienes que mejorar')  
    else:
        print('Buen comienzo') 
        
elif nivel == 2:
    if puntos < 30:
        print('Prodia hacerse mejor')
    else:
        print('Gran avance de nivel')
    
elif nivel == 3:
    if puntos < 40:
        print('Mejorable para un nivel avanzado')
    else:
        print('Impresionante')
    
else:
    print('Majestuoso, sigue así')