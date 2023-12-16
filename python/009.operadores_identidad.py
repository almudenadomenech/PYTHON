

# is

# None equivale a null o vacio

email = None #  nulo, No es texto, ni bool, ni númerico, no hay valor

user_email = input('Introduce tu email: ')

## endswith    Para evaluar las últimas letras por ejemplo el .com  
if user_email.endswith('@gmail.com'):
    email = user_email # Asignamos el user email solo si es de gmail.com
    
    
# llegados a este punto la variable email puede ser None o tener un valor

if email is None:
    print('Email incorrecto')

# is not

if email is not None:
    print('Correo resgistrado satisfactoriamente.')
    
# is
print(1 == True) # True
print(0 == True) # False
print ( 1 is True)# False no son idénticos por uno es int y tro es bool
