import math
from math import pi as pi

primer_numero = 45
segundo_numero = 15

# Operaciones ARITMÉTICAS
print(primer_numero + segundo_numero)
print(primer_numero - segundo_numero)
print(primer_numero * segundo_numero)
print(primer_numero / segundo_numero)
print(type(primer_numero / segundo_numero))

print(dir(primer_numero))
# is_integer responde TRUE si el número tiene una parte entera
print(primer_numero.is_integer())
division = 9 / 5
print(9/5)
# is_integer responde FALSE si el número tiene una valor en la parte decimal
print(division.is_integer())
# floor trunca el resultado de una operación o número
print(math.floor(9/5))
# round aproxima el resultado de una operación o número
print(round(9/5))
# sqrt calcula la raíz cuadrada de un número
print(math.sqrt(9))
# Eleva el número e a la potencia indicada como argumento
print(math.exp(5))

print(pi * 25)

print(dir(math))