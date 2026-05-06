# OPERADORES ARITMÉTICOS



# Operador SUMA +

# Permite SUMAR 2 valores numéricos
suma = 25 + 45
print(suma)

# Permite CONCATENAR (unir) 2 cadenas de texto
concatenacion = 'Hola' + ' ' + 'Queridos Estudiantes!'
print(concatenacion)


# Operador RESTA -

# Permite RESTAR 2 valores numéricos
resta = 25 - 45
print(resta)


# Operador MULTIPLICACIÓN *

# Permite MULTIPLICAR 2 valores numéricos
mutiplicacion = 25 * 45
print(mutiplicacion)

# Permite MULTIPLICAR una cadena de texto por un valor numérico
multiplicacion_2 = 'Hola' * 3
print(multiplicacion_2)

# Permite elevar un numero a una potencia
potencia = 2 ** 3
print(potencia)


# Operador DIVISIÓN /

# Permite DIVIDIR 2 valores numéricos
# Si el denominador es 0, la operación arrojará un error
# ZeroDivisionError
def division(a,b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print('No se puede DIVIDIR por 0')
    except Exception as error:
        print(f'Error en la operación: {error}')

division(25,0)

# Permite obtener el resto de una división
resto = 9.5 % 5.3
print(resto)


# Operador EQUIVALENTE
print('\nOperador EQUIVALENTE')
print(f'5 == 6 ? {5 == 6}')
print(f'3 == 9/3 ? {3 == 9/3}')

# Operador MAYOR QUE
print('\nOperador MAYOR QUE')
print(f'6 > 9 ? {6 > 9}')
print(f'6 > 3 ? {6 > 3}')

# Operador MAYOR O IGUAL QUE
print('\nOperador MAYOR O IGUAL QUE')
print(f'6 >= 3 ? {6 >= 3}')
print(f'6 >= 9 ? {6 >= 9}')
print(f'6 >= 12/2 ? {6 >= 12/2}')

# Operador MENOR QUE
print('\nOperador MENOR QUE')
print(f'6 < 9 ? {6 < 9}')
print(f'6 < 3 ? {6 < 3}')

# Operador MENOR O IGUAL QUE
print('\nOperador MENOR O IGUAL QUE')
print(f'6 <= 3 ? {6 <= 3}')
print(f'6 <= 9 ? {6 <= 9}')
print(f'6 <= 12/2 ? {6 <= 12/2}')

# Operador DISTINTO
print('\nOperador DISTINTO')
print(f'5 != 6 ? {5 != 6}')
print(f'3 != 9/3 ? {3 != 9/3}')


print('\nOperador Lógico O (or)')
print(f'V or V = {True or True}')
print(f'V or F = {True or False}')
print(f'F or V = {False or True}')
print(f'F or F = {False or False}')

print('\nOperador Lógico Y (and)')
print(f'V and V = {True and True}')
print(f'V and F = {True and False}')
print(f'F and V = {False and True}')
print(f'F and F = {False and False}')