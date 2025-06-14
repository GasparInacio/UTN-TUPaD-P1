"""
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
"""


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def ejercicio1():
    num_final = input('Ingresar un número entero positivo: ')
    try:
        num_final = int(num_final)
        if num_final > 0:
            for i in range(1, num_final + 1):
                print(f'{i}! = ', factorial(i))
        else:
            print('Debe ser un número entero positivo')
    except ValueError:
        print('Debe ser un numero entero positivo')


"""2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
especifique.
"""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def ejercicio2():
    posicion = input('Ingrese un número entero positivo: ')

    try:
        posicion = int(posicion)
        if posicion >= 0:
            for i in range(0, posicion + 1):
                print(f'{i} = ', fibonacci(i))
        else:
            print('Debe ser un numero entero positivo')
    except ValueError:
        print('Debe ser un numero entero positivo')


"""
3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
algoritmo general. 
"""


def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


def ejercicio3():
    try:
        base = int(input('ingrese un número para la base: '))
        exponente = int(input('ingrese un exponente para la base: '))

        if exponente >= 0:
            resultado = potencia(base, exponente)
            print(f'{base} ** {exponente} = {resultado}')
        else:
            print('El exponente debe ser un numero entero positivo')
    except ValueError:
        print('Debe ser un numero entero positivo')


"""
4) Crear una función recursiva en Python que reciba un número entero positivo en base 
decimal y devuelva su representación en binario como una cadena de texto.
"""


def binario(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return binario(n // 2) + str(n % 2)


def ejercicio4():
    num = input('Ingresar número entero positivo: ')

    try:
        num = int(num)
        if num >= 0:
            resultado = binario(num)
            print(f'Número en decimal {num} = {resultado} en binario')
        else:
            print('Ingrese un numero entero positivo')
    except ValueError:
        print('Debe ser un numero entero positivo')


"""
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
lo es. 
Requisitos: 
La solución debe ser recursiva. 
No se debe usar [::-1] ni la función reversed(). 
"""


def palindromo(palabra, izquierda=0, derecha=None):
    if derecha is None:
        derecha = len(palabra) - 1

    if izquierda >= derecha:
        return True
    elif palabra[izquierda] != palabra[derecha]:
        return False
    else:
        return palindromo(palabra, izquierda + 1, derecha - 1)


def ejercicio5():
    palabra = input('Ingresar palabra: ')

    if palindromo(palabra):
        print(f'{palabra} es palindromo')
    else:
        print(f'{palabra} no es palindromo')


"""
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
número entero positivo y devuelva la suma de todos sus dígitos. 
Restricciones: 
No se puede convertir el número a string. 
Usá operaciones matemáticas (%, //) y recursión. 
Ejemplos: 
suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
suma_digitos(9)      → 9 
suma_digitos(305)    → 8   (3 + 0 + 5) 
"""


def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)


def ejercicio6():
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero >= 0:
            resultado = suma_digitos(numero)
            print(f"La suma de los dígitos de {numero} es: {resultado}")
        else:
            print("Ingrese un número entero positivo.")
    except ValueError:
        print("Ingrese un número entero.")


"""
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
último nivel con un solo bloque. 
"""


def total_bloques(n):
    if n == 1:
        return 1
    else:
        return n + total_bloques(n - 1)


def ejercicio7():
    try:
        n = int(input("Ingresar el número de bloques del primer nivel: "))
        if n >= 1:
            total = total_bloques(n)
            print(f"El total de bloques en la pirámide es: {total}")
        else:
            print("Debe ingresar un número entero positivo.")
    except ValueError:
        print("Ingrese un número entero positivo.")


"""8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
aparece ese dígito dentro del número. 
      Ejemplos: 
contar_digito(12233421, 2)   → 3   
contar_digito(5555, 5)       → 4  
"""


def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)


def ejercicio8():
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        digito = int(input("Ingrese el dígito que quiere contar: "))

        if 0 <= digito <= 9:
            resultado = contar_digito(numero, digito)
            print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")
        else:
            print("El dígito debe estar entre 0 y 9.")
    except ValueError:
        print("Ingresar un número entero y un dígito entre 0 y 9.")
