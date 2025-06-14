"""
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}


def ejercicio1():
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300

    print(precios_frutas)


"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
● Banana = 1330 
● Manzana = 1700 
● Melón = 2800 
"""


def ejercicio2():
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800

    print(precios_frutas)


"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
precios. 
"""


def ejercicio3():
    frutas = list(precios_frutas.keys())
    print(frutas)


"""
4) Escribí un programa que permita almacenar y consultar números telefónicos. 
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
• Luego, pedí un nombre y mostrale el número asociado, si existe. 
"""

contactos = {}


def agregar():
    for i in range(5):
        nombre = input("Ingresar nombre: ")
        numero = input("Ingresar numero: ")
        try:
            numero = int(numero)
        except ValueError:
            print('Deben ser números')
        contactos[nombre] = numero
        i += 1


def buscar():
    name = input("Ingresar nombre: ")
    if name in contactos:
        print(f'contacto: {name} = {contactos[name]}')
    else:
        print('No existe contacto')


def ejercicio4():
    agregar()
    buscar()


"""
5) Solicita al usuario una frase e imprime: 
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra. 
"""


def ejercicio5():
    frase = input("Ingresar frase: ")
    palabras = frase.split()
    palabras_unicas = set(palabras)
    print(f'Palabras unicas: {palabras_unicas}')

    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    print(f'Conteo de palabras: {frecuencia}')


"""
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
Luego, mostrá el promedio de cada alumno. 
"""


def ejercicio6():
    notas = {}
    for i in range(3):
        nombre = input("Ingresar nombre: ")
        nota1 = input("Ingresar nota1: ")
        nota2 = input("Ingresar nota2: ")
        nota3 = input("Ingresar nota3: ")
        i += 1
        notas[nombre] = (nota1, nota2, nota3)

    print('promedios')

    for alumno, notas in notas.items():
        promedio = sum(notas[alumno]) / 3
        print(f'{alumno}: {promedio:2f}')


"""
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
y Parcial 2: 
• Mostrá los que aprobaron ambos parciales. 
• Mostrá los que aprobaron solo uno de los dos. 
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 
"""


def ejercicio7():
    set1 = {8, 6, 10}
    set2 = {7, 6, 9}

    ambos = set1.intersection(set2)
    print(f'Ambos: {ambos}')
    solo_uno = set1.symmetric_difference(set2)
    print(f'Solo uno: {solo_uno}')
    al_menos_uno = set1.union(set2)
    print(f'Al menos uno: {al_menos_uno}')


"""
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
Permití al usuario: 
• Consultar el stock de un producto ingresado. 
• Agregar unidades al stock si el producto ya existe. 
• Agregar un nuevo producto si no existe. 
"""


def ejercicio8():
    stock = {
        'Tomate': 10,
        'Pan': 20,
        'Palta': 30
    }

    print('Stock de productos: ')

    buscar = input('Ingresar nombre de producto: ')

    if buscar in stock:
        print(f'El stock de {buscar} es {stock[buscar]}')

    agregar = input('Ingresar nombre de producto a agregar: ')

    agregar_stock = input('Ingresar cantidad a agregar')

    try:
        agregar_stock = int(agregar_stock)
    except ValueError:
        print('Ingresar número')

    stock[agregar] = agregar_stock

    print(f'stock productos: {stock}')


"""
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
Permití consultar qué actividad hay en cierto día y hora. 
"""

def ejercicio9():
    agenda = {
        ('Lunes', '10:00'): 'Reunión',
        ('Martes', '14:00'): 'Clase',
        ('Miércoles', '09:00'): 'Consulta médica',
        ('Viernes', '18:30'): 'Entrenamiento'
    }

    dia = input('Ingresar dia: ')
    hora = input('Ingresar hora (ej 12:40): ')

    clave = (dia, hora)

    if clave in agenda:
        print(f'Actividad el {dia} a las {hora} horas: {agenda[clave]}')

"""
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
diccionario donde: 
• Las capitales sean las claves. 
• Los países sean los valores.
"""

def ejercicio10():
    original = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago'}

    invertido = {capital: pais for pais, capital in original.items()}

    print(f'Original: {original}')
    print(f'Invertido: {invertido}')