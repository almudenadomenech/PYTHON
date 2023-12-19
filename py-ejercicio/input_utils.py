# Funciones para leer por consola con input con GESTIÓN DE EXCEPCIONES

def read_int(prompt):
    while True:
        try:
            
            resultado = int(input(prompt))
            return resultado # sale del bucle y devuelve el resultado
        except Exception:
            print('Error al leer entrada')
            
# edad= read_int('Introduce tu edad: ')
# altura = read_int('Introduce tu altura: ')
# peso = read_int('Introduce tu peso')
# print(f'Tu edad es {edad}')
# print(f'Tu edad es {altura}')
# print(f'Tu edad es {peso}')
# print('FIN')       

            
def read_float(prompt):
     while True:
        try:
            
            resultado = float(input(prompt))
            return resultado # sale del bucle y devuelve el resultado
        except Exception:
            print('Error al leer entrada')
            

# salario= read_float('Introduce salario: ')
# precio = read_float('Introduce pecio: ')
# print(f'El salario es {salario}')
# print(f'El precio es {precio}')
# print('FIN') 



def read_bool(prompt):
    while True:
        try:
            resultado =(input(prompt)) 
            if resultado == 'si':
                return True
            elif resultado == 'no':
                return False
            else:
                print('valor no reconocido, inténtalo denuevo.')
        except Exception:
            print('Error al leer la entrada. Intentalo de nuevo')
    

# alta = read_bool('Esta dado de alta si/no:')
#print(f'alta {alta}') 

def read_email():
    pass