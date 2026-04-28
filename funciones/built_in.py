import math
# BUILT IN son funciones que ya existen dentro del lenguaje

# PRINT es una función que muestra por pantalla (terminal o línea de comandos) el argumento entregado
print('Este es el ARGUMENTO de la función')

# El MÉTODO (o función) ROUND redondea un número a una cantidad específica de decimales
print(round(math.pi,3))

lista_numeros = [10,20,30,40,50]
# EL método SUM realiza una suma de elementos de tipo número, entregados como argumento
print(sum(lista_numeros))
print(sum([1,5,9,7,5,3]))

# El método INPUT permite al usaurio ingresar datos, que SIEMPRE serán de tipo STRING
nombre = input('Ingrese su nombre:')
print(nombre)