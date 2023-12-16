
# if
# if else
# if elif else

precio =float(input('introduce precio: '))


if precio> 100: # <= 100 es caro
    print('El producto es caro')
elif precio>= 50: # <= 50 es medio
    print('El precio es normal/medio')
else: # es barato
    print('es barato')

print('fin')

# RUTINA DIARIA
# Para emojis en windows: tecla windows + `
# o buscar en https://emojicopy.com
hora= int(input('Introduce una hora: '))

if 0 <= hora <= 8:
    print('Durmiendo... zzz...😴')
elif 8 < hora <= 15:
    print('Curso Angular')
elif 15 < hora <= 18:
    print('Comiendo paella  ')
elif 18 < hora <= 21:
    print('En el gimnasio')
elif 21 < hora <= 24:
    print('cenando')
else:
    print('la hora no es correcta')