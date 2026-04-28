# Tipos de datos en Python

print(type(5))
print(type(3.2))
print(type('Hola'))
print(type(True))

# La variable numero_real almacenará un dato de número entero
numero_entero = 0
numero_decimal = 0.0
cadena_texto = "Buen día queridos estudiantes!"
valor_booleano = False

print("Mi primer mensaje en Python")

print()
print(numero_entero)
print(type(numero_entero))

print()
print(numero_decimal)
print(type(numero_decimal))

print()
print(cadena_texto)
print(type(cadena_texto))

print()
print(valor_booleano)
print(type(valor_booleano))

valor_booleano = 5 > 3
print()
print(valor_booleano)
print(type(valor_booleano))

cadena_texto = 'Incluir comilla con caracter de escape \'...'
cadena_texto_2 = 'Incluir comilla sin carcater de escape "'
print(cadena_texto)
print(cadena_texto_2)

# CONCATENACIÓN de cadenas de texto
saludo = 'Buen día querido '
nombre = 'Erick Bailey'
print()
print(saludo + nombre)

texto_una_linea_comillas_simples = 'texto de una línea'
texto_una_linea_comilla_dobles = "texto de una línea"

texto_multiples_lineas_comillas_simples = '''
línea 1 texto de múltiples líneas
línea 2 texto de múltiples líneas
línea 3 texto de múltiples líneas
'''
texto_multiples_lineas_comilla_dobles = """
línea 1 texto de múltiples líneas
línea 2 texto de múltiples líneas
línea 3 texto de múltiples líneas
"""

print(texto_multiples_lineas_comilla_dobles)