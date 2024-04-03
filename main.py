def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Función para validar que el número ingresado sea un entero positivo
def validar_entero_positivo(numero):
    try:
        num = int(numero)
        if num <= 0:
            raise ValueError("Debes ingresar un número entero positivo.")
        return num
    except ValueError:
        raise ValueError("Debes ingresar un número entero positivo.")

# Solicitar al usuario que ingrese los números y validar la entrada
while True:
    try:
        num1 = validar_entero_positivo(input("Ingresa el primer número entero positivo: "))
        num2 = validar_entero_positivo(input("Ingresa el segundo número entero positivo: "))
        break
    except ValueError as ve:
        print(ve)

# Calcular el MCD
mcd = calcular_mcd(num1, num2)

# Mostrar el resultado
print("El máximo común divisor de", num1, "y", num2, "es:", mcd) 