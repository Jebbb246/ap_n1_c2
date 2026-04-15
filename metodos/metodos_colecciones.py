#Métodos para trabajar con listas

animales = ['Gato','Perro','Vaca','Conejo','Ornitorrinco','Murciélago']
frutas = ['Durazno','Fresa','Mango','Melón']

# El método APPEND agrega elementos al final de la lista
print(animales)
nuevo_animal = input('Agregue un nuevo animal a la lista: ')
animales.append(nuevo_animal)
print(animales)

print(len(animales))
# El método INSERT agrega un elemento en la posición indicada
otro_nuevo_animal = input('Agregue un nuevo animal a la lista: ')
animales.insert(0,otro_nuevo_animal)
print(animales)

# El método EXTEND permite agregar varios elementos a una lista
animales.extend(['Oveja','Cerdo'])
print(animales)
animales.extend(frutas)
print(animales)