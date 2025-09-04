try:
    numero = int(input("Ingrese un número: "))
    
    if numero <= 0:
        print("Error: El número debe ser mayor que cero.")
    else:
        suma = 0
        for i in range(1, numero + 1):
            suma += i
        
        print(f"La sumatoria de los números entre 1 y {numero} es: {suma}")

except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")