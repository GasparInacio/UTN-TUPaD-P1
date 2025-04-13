import random


def ejercicio_1():
    """1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
    (incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

    for i in range(101):
        print(i)


def ejercicio_2():
    """2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
    dígitos que contiene."""

    num = input("Ingrese un número entero: ")

    try:
        num = int(num)
        digitos = 0
        if num < 0:
            num = num * -1

            if num == 0:
                print("La cantidad de dígitos es: 1")
            else:
                while num > 0:
                    num = num // 10
                    digitos += 1

                print(f"La cantidad de dígitos es: {digitos}")
    except ValueError:
        print("Por favor ingrese un valor numérico")


def ejercicio_3():
    """3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
    dados por el usuario, excluyendo esos dos valores."""

    num1 = input("ingresse un número: ")
    num2 = input("ingresse otro número: ")

    if num1 > num2:
        try:
            num2 = int(num2)
            num1 = int(num1)
            num2 = num2 + 1
            contador = 0
            for i in range(num2, num1):
                contador += i
            print(
                f"La suma de los números entre {num2} y {num1} excluyendo esos dos valores es: {contador}"
            )
        except ValueError:
            print("Los valores tienen que ser numéricos")
    else:
        try:
            num2 = int(num2)
            num1 = int(num1)
            num1 = num1 + 1
            contador = 0
            for i in range(num1, num2):
                contador += i
            print(
                f"La suma de los números entre {num2} y {num1} excluyendo esos dos valores es: {contador}"
            )
        except ValueError:
            print("Los valores tienen que ser numéricos")


def ejercicio_4():
    """4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
    secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
    un 0."""

    res = 0

    while True:
        num = input("Ingrese un número para sumar (0 para salir): ")

        try:
            num = int(num)
        except ValueError:
            print("Debe ingresar un valor numerico")
            continue
        if num == 0:
            break

        res += num
        print(f"El resultado es: {res}")


def ejercicio_5():
    """5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
    programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

    inc = random.randint(0, 9)
    contador = 0

    while True:
        num = input("Adivine el número de 0 a 9: ")
        try:
            num = int(num)
            if num != inc:
                contador += 1
            else:
                print(f"Lo adivinaste! Era {inc}")
                print(f"Cantidad de intentos: {contador}")
                break
        except ValueError:
            print("Debe ingresar un valor numérico")
            continue


def ejercicio_6():
    """6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
    entre 0 y 100, en orden decreciente."""

    for i in range(100, -1, -2):
        print(i)


def ejercicio_7():
    """7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
    número entero positivo indicado por el usuario."""

    res = 0

    while True:
        num = input("Ingrese un número para el rango máximo: ")
        try:
            num = int(num)
        except ValueError:
            print("Ingrese un valor numérico")
            continue
        if num < 0:
            print("Ingrese un número positivo distinto de 0: ")
            continue
        else:
            for i in range(0, (num + 1)):
                res += i

            print(f"El resultado de sumar cada número desde 0 a {num} es: {res}")
            break


def ejercicio_8():
    """8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
    programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
    negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
    menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

    pares = 0
    impares = 0
    positivos = 0
    negativos = 0

    chances = 100
    contador = 0

    while contador < chances:
        num = input("Ingrese un número: ")

        try:
            num = int(num)
        except ValueError:
            print("Debe ingresar un valor numerico")
            continue

        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

        if num >= 0:
            positivos += 1
        else:
            negativos += 1

        contador += 1

    print(
        f"Números pares: {pares}\nNúmeros impares: {impares}\nNúmeros positivos: {positivos}\nNúmeros negativos: {negativos}"
    )


def ejercicio_9():
    """9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
    media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
    poder procesar 100 números cambiando solo un valor)."""

    chances = 5
    contador = 0
    suma = 0

    while contador < chances:
        num = input("Ingrese un número: ")

        try:
            num = int(num)
        except ValueError:
            print("Debe ingresar un valor numerico")
            continue

        suma += num

        contador += 1

    media = int(suma / chances)
    print(f"La media de los números ingresados es: {media}")


def ejercicio_10():
    """10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
    usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

    while True:
        try:
            num = int(input("Ingrese un número: "))
        except ValueError:
            print("Debe ingresar un valor numerico")
            continue
        if num < 0:
            num = -num
            num = str(num)
            inv = num[::-1]
            print(f"-{inv}")
            break
        else:
            num = str(num)
            inv = num[::-1]
            print(inv)
            break
