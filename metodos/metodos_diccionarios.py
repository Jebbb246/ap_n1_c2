# Definamos un nuevo diccionario

datos_personales = {
    'nombre':'Agustín Riquelme',
    'edad':18,
    'titulo':'Analista Programador'
}

print(datos_personales)

# El método KEYS permite obtener las claves del diccionario dict_keys
claves = datos_personales.keys()
print(claves)

# El método GET permite obtener valores de datos por su clave
nombre = datos_personales.get('nombre')
print(nombre)

# Agregamos elementos al diccionario definiendo una nueva clave con un nuevo valor
rut = input('Ingrese su número de rut: ')
datos_personales['rut'] = rut
print(datos_personales)

# El método POP elimina un elemento por su clave
datos_personales.pop('rut')
print(datos_personales)