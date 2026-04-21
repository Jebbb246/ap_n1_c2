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
    
# Para evaluar varias condiciones usamos IF con ELIF
# Clase Alta ÉliteSobre $7.000.000
# Clase Alta Profesional $3.500.000 - $7.000.000
# Clase Media Alta $2.000.000 - $3.500.000
# Clase Media $1.200.000 - $2.000.000
# Clase Media Baja $700.000 - $1.200.000
# Clase Baja Menos de $600.000

str_sueldo_mensual = input('Ingrese su sueldo mensual: $')
sueldo_mensual = float(str_sueldo_mensual)

if sueldo_mensual > 7000000:
    print('Ud. pertenece al grupo Alta Elite')
elif 3500000 < sueldo_mensual <= 7000000:
    print('Ud. pertenece al grupo Alta Profesional')
elif 2000000 < sueldo_mensual <= 3500000:
    print('Ud. pertenece al grupo Media Alta')
elif 1200000 < sueldo_mensual <= 2000000:
    print('Ud. pertenece al grupo Media Emergente')
else:
    print('Sueldo ingresado NO corresponde...')