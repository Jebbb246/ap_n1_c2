# Cada dato ingresado mediante input ES un TEXTO

numero = input('Por favor, ingrese un número entero...')
print(type(numero))
print(numero)

print(f'Su NÚMERO multiplicado por 4 es : {numero * 4}')
print(f'Su NÚMERO (convertido a decimal) multiplicado por 2 es : {float(numero) * 2}')
print(f'Su NÚMERO (convertido a entero) multiplicado por 2 es : {int(numero) * 2}')



saludo = 'Buen día querido '
nombre = input('Ingrese su nombre: ')
print()
print(saludo + nombre)

# Ingrese 2 números mediante su teclado y muestre el resultado de la suma
print('Vamos a sumar 2 números enteros')
numero_1 = 0
numero_2 = 0
resultado = 0

# Convirtiendo los textos ingresados en NÚMEROS
numero_1 = int(input('Ingrese el primer número entero: '))
numero_2 = int(input('Ingrese el segundo número entero: '))

# Después de convertir a número, viene la operación aritmética
resultado = numero_1 + numero_2

# Mostramos el resultado, para cooncatenar el número de la variable resultado, lo convertimos en texto
print('El resultado de la suma es: ' + str(resultado))

# Concatenación FORMATEANDO como cadena de texto
print(f'El resultado de la suma es: {resultado}')
print(f'{numero_1} + {numero_2} = {resultado}')