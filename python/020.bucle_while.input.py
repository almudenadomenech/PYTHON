

passwor_correct = "admin"
password = ""

while password != passwor_correct:
    password = input('Introduce la password: ').replace(" ", "")

print('credenciales correctas')

# Mientras que el departament escrito por el usuario no esté
# en la lista de departamentos posibles entoncesle seguimos
# preguntando por el departamento

departamentos = ['marketing', 'desarrollo', 'soporte', 'ia']
departamento = ''

while departamento not in departamentos:
    departamento =input ('Introduce el departamento: ')

print('Departameto correcto')