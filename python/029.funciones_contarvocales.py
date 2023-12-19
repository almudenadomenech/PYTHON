

def contar_vocales(texto):
   # for
   # if
   # in
   # return
   num_vocales = 0
   
   for caracter in texto:
       if caracter.lower() in 'a, e, o, u':
        num_vocales += 1
       
   return num_vocales   
        
        
   
num_vocales1 = contar_vocales('Almudena')
print(num_vocales1)

num_vocales2 = contar_vocales('Hola mundo')
print(num_vocales2)