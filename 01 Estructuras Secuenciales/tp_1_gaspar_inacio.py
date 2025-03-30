'''Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. '''

print('“Hola Mundo!”')

'''Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
realizar la impresión por pantalla. '''

nombre = input('Ingrese su nombre: ')
print(f'Hola {nombre}!')

'''Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
la impresión por pantalla. '''

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = input('Ingrese su edad: ')
lugar_residencia = input('Ingrese su lugar de residencia: ')
print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}')

'''Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
su perímetro.'''

radio = float(input('Ingrese el radio del círculo: '))
pi = 3.14159
area = pi * (radio * radio)
perimetro = 2 * pi * radio
print(f'El área del círculo es: {area}')
print(f'El perímetro del círculo es: {perimetro}')

'''Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
cuántas horas equivale. '''

segundos = int(input('Ingrese la cantidad de segundos: '))
hora = segundos // 3600
print(f'Los segundos equivalen a {hora} horas')

'''Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
multiplicar de dicho número. '''

numero = int(input('Ingrese un número: '))

for i in range(1, 11):
    print(f'{numero} * {i} = {numero * i}')

'''Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. '''

num1 = int(input('Ingrese un número distinto de 0: '))
num2 = int(input('Ingrese otro número distinto de 0: '))
suma= num1 * num2
resta = num1 - num2
multiplicaciom = num1 * num2
division = round((num1 * num2), 2)
print(f'El resultado de la suma de los números es: {suma}')
print(f'El resultado de la resta de los números es: {resta}')
print(f'El resultado de la multiplicaciom de los números es: {multiplicaciom}')
print(f'El resultado de la division de los números es: {division}')

'''Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
de masa corporal. '''

altura = float(input('Ingrese su altura en mts: '))
peso = int(input('Ingrese su peso en kg: '))
imc = round(peso / (altura ** 2), 2)
print(f'Su índice de masa corporal es {imc}')

'''Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
pantalla su equivalente en grados Fahrenheit. '''

temperatura_celcius = float(input('Ingrese la temperatura en °C: '))
farenheit = round(((9 / 5) * temperatura_celcius + 32), 2)
print(f'{temperatura_celcius}°C equivalen a {farenheit}°F')

'''Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
dichos números. '''

num1 = float(input('Ingrese un número: '))
num2 = float(input('Ingrese un segundo número: '))
num3 = float(input('Ingrese un tercer número: '))
promedio = round(((num1 + num2 + num3) / 3), 2)
print(f'El promedio de los números ingresados es: {promedio}')