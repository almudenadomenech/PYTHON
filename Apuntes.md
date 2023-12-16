## TIPOS DE DATOS

# Número Enteros (int)

numero_entero = 42

# Números de coma flotante (float)

número_flotante = 3.14

# Números complejos (complex)

numero_complejo = 5 + 3j

# Cadenas de caracteres (str)

cadena = "Hola, mundo"
cadena = ' Hola mundo'

cadena multilinea = """
Esto es una línea
Estos es otra línea
Estos es otra línea."""

# Valores booleanos (bool)

 valor_booleano1 = True
 valor_booleano2 = False

## TIPOS DE DATOS COMPUESTOS

# Listas (list)

lista_numeros = [1, 2, 3, 4]

# Tuplas (tuple)

tupla_colores = ( "rojo", "verde", "azul")

# Conjuntos (set)

conjunto_de_frutas = { "manzana", "naranja"}

# Diccionarios (dict)
 
 diccionario_precios = {"manzana": 1.5, "naranja": 0.99}


 ## OPERADORES

 # Operadores aritméticos

 * Suma +
 * Resta -
 * Multiplicación *
 * División /
 * Módulo %: devuelve el resto de la división
 * Exponente **
 * División entera //

 # Operadores de comparación

 * Igual ==
 * Distinto !=
 * Mayor que >
 * Menor que <
 * Mayor o igual que >=
 * Menor o igual que <=

 # Operadores lógicos

 * and : devuelve True si ambos operadores son True.
 * or : decuelve True si al menos uno de los operandos es True.
 * not : devuelve True si el operando es False, y False si el operando es True.

 # Operadores de asignación

 * =  : Asignación simple 
 * += : Asignacion con suma
 * -= : Asignacion con resta
 * *= : Asignacion con multiplicación
 * /= : Asignacion con división
 * %= : Asignacion con módulo
 * **= : Asignacion con exponente
 * //= : Asignacion con división entera

# Operadores de identidad

Comparan la identidad de dosobjetos (no su valor) devuelve un valor booleano

* is: devuelve True si ambos objetos son el mismo objeto
* is not: devuelve True si ambos objetos no son el mismo objeto.

# Operadores de membresia

Verifican si un valor es miemvro de una secuencia, como cadenas de caracteres, 
listas o truplas, y devuelven un valor booleano.

* in: devuelve True si el valor especificado se encuentra en la secuencia.
* not in: devuelve True si el valor especificado no se encuantra en la secuencia.


### ESTRUCTURAS DE CONTROL

## CONDICIONALES

# if
 La declaración if evalúa una condición y ejecuta un bloque de código si la condición es verdadera
 (True).

    edad = 18
    if edad >= 18:
     print("Eres mayor de edad")

# elif
  La declaración elif (abreviatura de "else if") se utiliza junto con if para verificar múltiples
  condiciones

   edad = 16
   if edad >= 18:
   print("Eres mayor de edad")
   elif edad >= 16:
   print("Eres menor de edad pero puedes obtener un permiso de conducir")

# else
 La declaración else se utiliza junto con if y elif para proporcionar una opción por defecto cuando
 todas las condiciones anteriores son falsas (False).

  edad = 15
 if edad >= 18:
 print("Eres mayor de edad")
 elif edad >= 16:
 print("Eres menor de edad pero puedes obtener un permiso de conducir")
 else:
 print("Eres menor de edad")  

 ## Expresiones condicionales (operador ternario)

 Las expresiones condicionales permitin asignar un valor a una variable basándose en una condición, 
 en una sola línea de código.

 Determinar el valor absoluto de un número:
  numero = -5
 valor_absoluto = numero if numero >= 0 else -numero
 print(valor_absoluto)






