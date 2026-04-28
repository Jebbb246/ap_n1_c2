# Dentro del lenguaje, tenemos la opción de crear nuestras PROPIAS funciones
# para eso usamos la palabra reservada DEF

def suma(a,b):
    # Este será el contenido de la función
    resultado = a + b
    print(resultado)

def resta(a,b):
    resultado = a - b
    print(resultado)

def multiplicacion(a,b):
    resultado = a * b
    print(resultado)

def division(a,b):
    if b == 0:
        print('No se puede dividir por 0')
    else: 
        resultado = a/b
        print(resultado)

def pedir_datos():
    numero_1 = input('Ingrese primer número: ')
    numero_2 = input('Inrese segundo número: ')
    return(numero_1, numero_2)

def validar_numeros(num_1,num_2):
    if num_1.isdigit() and num_2.isdigit():
        num_1 = float(num_1)
        num_2 = float(num_2)
    else:
        print('Valor NO corresponde a un número')
    return

    suma(num_1,num_2)
    resta(num_1,num_2)
    multiplicacion(num_1,num_2)
    division(num_1,num_2)