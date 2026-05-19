# Teniendo 3 escalas de temperatura (Celsius, Fahrenheit, Kelvin)
# Cree un conversor de temperaturas que le pida al usuario la temperatura  y escala inicial
# Y la escala que desea convertir, luego muestre el resultado de la conversión

# °C a °F = °C * 1,8 + 32
# °F a °C = (°F - 32) / 1,8
# °C a K = °C + 273
# K a °C = K - 273
# °F a K = (°F - 32) / 1,8 + 273
# K a °F = (K - 273) * 1,8 + 32

print('"C" para Celsius')
print('"F" para Fahrenheit')
print('"K" para Kelvin')
escala_inicial = input('Indique la escala inicial: ')
str_temperatura = input('Ingrese la temperatura: ')
escala_final = input('Indique la escala final: ')

#if str_temperatura.isdigit():
#    temperatura = float(str_temperatura)
#else:
#    print('El valor de la temperatura no corresponde')

if escala_inicial == 'F':
    if escala_final == 'K':
        resultado = 

    pass
elif escala_inicial == 'C':
    pass
elif escala_inicial == 'K':
    pass
else:
    print('Ingrese un valor válido')