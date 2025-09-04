try:
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))

    if num1 < num2:
        menor = num1
        mayor = num2
    else:
        menor = num2
        mayor = num1

    suma = 0
    contador = menor + 1

    while contador < mayor:
        suma += contador
        contador += 1

    print(f"La suma de los números entre {num1} y {num2} es: {suma}")

except ValueError:
    print("Error: Por favor, ingrese solo números enteros.")