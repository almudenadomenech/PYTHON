

# in

print("A" in "Almudena") # True
print("A" in "Luis") # False

print("Angular" in "Curso desarrollo web con Angular") # True
print("Python" in "Curso desarrollo web con Angular") # False

# not in

print("sex" not in "Hola buenos días")

# in con lista
# Comprueba si un estudiante está dentro de la lista de estudiantes admitidos
students =['Adrian', 'Albora', 'Eunice', 'Jana']
student = input('Introduce tu nombre: ')

if student in students:
    print("Tienes acceso al curso de Angular")
else:
    print('Lo siento, no eres VIP')