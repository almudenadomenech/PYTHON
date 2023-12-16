
# METODO remove()
names = ['Ana','Diego', 'Gema', 'Alan']

names.remove('Alan')

# names.remove('Alan') # da un error. Si intentas borrar algo que no esxiste
print(names)

# METODO pop () : elimina y devuelve un elemento de la lista por su índice, por defecto el último
names = ['Ana','Diego', 'Gema', 'Alan', 'Albora', 'Raquel']

ultimo= names.pop() # sin índice te devuelve el último

print(names)
diego = names.pop(1)
print(names)

# PALABRA RESERVADA del
names = ['Ana','Diego', 'Gema', 'Alan', 'Albora', 'Raquel']
del names[0]
print(names)
