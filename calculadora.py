num1 = int(input("Escriba el primer número: "))
num2 = int(input("Escriba el segundo número: "))

def sumar():
    print("El resultado de su suma es:")
    print(num1 + num2)

def restar():
    print("El resultado de su resta es:")
    print(num1 - num2)

def multiplicacion():
    print("El resultado de su multiplicación es:")
    print(num1 * num2)

print("Seleccione la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")

opcion = int(input("Elija una opción (1/2/3): "))

if opcion == 1:
    sumar()
elif opcion == 2:
    restar()
elif opcion == 3:
    multiplicacion()
else:
    print("Opción no válida. Por favor, elija una opción válida (1/2/3).")