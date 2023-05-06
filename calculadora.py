import math

while True:
    print("\n*** Calculadora ***")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Factorial")
    print("7. Raíz cuadrada")
    print("8. Cambiar números")
    print("9. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print(f"El resultado es: {resultado}")
    elif opcion == 2:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        print(f"El resultado es: {resultado}")
    elif opcion == 3:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 * num2
        print(f"El resultado es: {resultado}")
    elif opcion == 4:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 and num1 != 0:
            resultado = num1 / num2
            print(f"El resultado es: {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    elif opcion == 5:
        num1 = float(input("Ingrese el número base: "))
        num2 = float(input("Ingrese el exponente: "))
        resultado = num1 ** num2
        print(f"El resultado es: {resultado}")
    elif opcion == 6:
        num = int(input("Ingrese un número entero: "))
        resultado = math.factorial(num)
        print(f"El factorial de {num} es: {resultado}")
    elif opcion == 7:
        num = int(input("Ingrese un número entero positivo: "))
        if num >= 0:
            resultado = math.sqrt(num)
            print(f"La raíz cuadrada de {num} es: {resultado}")
        else:
            print("Error: El número debe ser entero positivo.")
    elif opcion == 8:
        continue
    elif opcion == 9:
        print("Gracias por usar la calculadora.")
        break
    else:
        print("Error: Opción inválida. Intente de nuevo.")