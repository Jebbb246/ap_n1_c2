str_edad = input('Ingrese su edad: ')
edad = int(str_edad)

# Condicional IF
if edad >= 18:
    # Este set de acciones se ejecuta cuando la respuesta es V
    print('Usted es mayor de edad')
else: 
    # Este set de acciones se ejecuta cuando la respuesta es F
    print('Usted es menor de edad')

# Solicite al usuario el ingreso de datos personales (nombre, edad y título)
# Si el usuario es mayor de edad, muestre por pantalla todos sus datos
# Si el usuario NO es mayor de edad, muestre un mensaje indicando que es menor de edad

nombre = input('Ingrese su nombre: ')
edad_a = int(input('Ingrese su edad: '))
titulo = input('Ingrese su titulo: ')

if edad_a >= 18:
    print('Su nombre es:', nombre)
    print('Su edad es:', edad_a)
    print('Su titulo es:', titulo)
else:
    print('Usted es menor de edad')