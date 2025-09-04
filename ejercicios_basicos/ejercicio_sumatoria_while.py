try:
    numero = int(input("Ingrese un número: "))
    
    if numero <= 0:
        print("Error: El número debe ser mayor que cero.")
    else:
        suma = 0
        contador = 1
        while contador <= numero:
            suma += contador
            contador += 1
        
        print(f"La sumatoria de los números entre 1 y {numero} es: {suma}")

except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")