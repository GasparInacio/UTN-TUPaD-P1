import math

# Al final del archivo se encuentra una función principal para mostrar todos los ejercicios juntos


"""1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""


def imprimir_hola_mundo():
    print("\nHola Mundo!")


"""2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""


def saludar_usuario(nombre):
    print(f"\nHola {nombre}!")


"""3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residenciPa]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados."""


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"\nSoy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados."""


def calcular_area_circulo(radio):
    area = math.pi * (radio**2)
    print(f"\nEl área del circulo con radio {radio} es: {area:.2f}")


def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"\nEl perímetro del círculo con radio {radio} es: {perimetro:.2f} ")


"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función."""


def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"\n{segundos} segundos equivalen a {horas:.2f} horas")


"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función."""


def tabla_multiplicar(numero):
    print(f"\nTabla del {numero}")
    for i in range(1, 11):
        print(f"{numero}*{i}={numero * i}")


"""7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara."""


def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a / b

    print(
        f"\nOperaciones básicas con los números {a} y {b}:\nsuma: {suma}\nresta: {resta}\nmultiplicación: {mult}\ndivisión: {div:.2f}"
    )


"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales."""


def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    print(f"\nSu IMC es: {imc:.2f}")


"""9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""


def celcius_a_farenheit(celcius):
    frh = (celcius * (9 / 5)) + 32
    print(f"\n{celcius}°C equivalen a {frh:.2f}°F")


"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función."""


def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"\nEl promedio de las notas ingresadas es: {promedio:.2f}")


def programa_principal():
    """
    Función principal para mostrar los ejercicios
    """

    while True:
        # Presentar las opciones
        print("\n#####################\nEjercicios funciones\n#####################\n")
        print(
            "1. Ejercicio 1\n2. Ejercicio 2\n3. Ejercicio 3\n4. Ejercicio 4\n5. Ejercicio 5\n6. Ejercicio 6\n7. Ejercicio 7\n8. Ejercicio 8\n9. Ejercicio 9\n10. Ejercicio 10"
        )
        # Ingreso de elección a visualizar
        try:
            selec = int(
                input("Ingrese el ejercicio que quiera visualizar o '0' para salir: ")
            )
        except ValueError:
            print("\nPor favor ingrese un valor numérico")
            continue

        if selec == 0:
            print("\nSaliendo...")
            break

        # Visualizaciones
        while True:
            if selec == 1:
                imprimir_hola_mundo()
                break
            elif selec == 2:
                nmbr = input("\nIngrese su nombre: ")
                saludar_usuario(nmbr)
                break
            elif selec == 3:
                nombre = input("\nIngrese su nombre: ")
                apellido = input("Ingrese su apellido: ")
                try:
                    edad = int(input("Ingrese su edad: "))
                except ValueError:
                    print("\nLa edad debe ser un valor numérico.")
                    continue
                residencia = input("Ingrese su lugar de residencia: ")
                informacion_personal(nombre, apellido, edad, residencia)
                break
            elif selec == 4:
                try:
                    radio = float(input("\nIngrese el radio del círculo: "))
                except ValueError:
                    print("\nPor favor ingrese un valor numérico.")
                    continue
                calcular_area_circulo(radio)
                calcular_perimetro_circulo(radio)
                break
            elif selec == 5:
                try:
                    segs = int(
                        input(
                            "\nIngrese la cantidad de segundos para convertirlos en horas: "
                        )
                    )
                except ValueError:
                    print("\nPor favor ingrese un valor numérico.")
                    continue
                segundos_a_horas(segs)
                break
            elif selec == 6:
                try:
                    num = int(
                        input(
                            "\nIngrese un número para saber la tabla de multiplicar: "
                        )
                    )
                except ValueError:
                    print("\npor favor ingrese un valor numérico.")
                    continue
                tabla_multiplicar(num)
                break
            elif selec == 7:
                try:
                    num1 = int(
                        input("\nIngrese un número para hacer operaciones básicas: ")
                    )
                    num2 = int(
                        input("Ingrese otro número para hacer operaciones básicas: ")
                    )
                except ValueError:
                    print("\nLos valores deben ser numéricos")
                    continue
                operaciones_basicas(num1, num2)
                break
            elif selec == 8:
                try:
                    peso = int(input("\nIngrese su peso (Kg): "))
                    altura = float(input("Ingrese su altura (mts): "))
                except ValueError:
                    print("\nLos valores deben ser numéricos")
                    continue
                calcular_imc(peso, altura)
                break
            elif selec == 9:
                try:
                    temp = float(
                        input(
                            "\nIngrese la temperatura en °C para transformarla en °F: "
                        )
                    )
                except ValueError:
                    print("\nEl valor debe ser numérico")
                    continue
                celcius_a_farenheit(temp)
                break
            elif selec == 10:
                try:
                    nota1 = float(input("\nIngrese la primer nota a promediar: "))
                    nota2 = float(input("Ingrese la segunda nota a promediar: "))
                    nota3 = float(input("Ingrese la tercer nota a promediar: "))
                except ValueError:
                    print("\nLos valores deben ser numéricos.")
                    continue
                calcular_promedio(nota1, nota2, nota3)
                break


programa_principal()
