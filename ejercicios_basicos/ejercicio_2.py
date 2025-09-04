def calcular_salario_mecanico():
    """
    Calcula el salario bruto semanal y las horas adicionales de un mecánico.
    """
    try:
        # Solicitar datos al usuario
        valor_hora = float(input("Ingresa el valor de la hora de trabajo: "))
        horas_trabajadas = float(input("Ingresa la cantidad de horas trabajadas en la semana: "))

        # Validar que los valores sean positivos
        if valor_hora < 0 or horas_trabajadas < 0:
            print("Error: El valor de la hora y las horas trabajadas deben ser números positivos.")
            return

        horas_adicionales = 0

        # Lógica para calcular el salario
        if horas_trabajadas > 40:
            horas_adicionales = horas_trabajadas - 40
            salario_normal = 40 * valor_hora
            salario_adicional = horas_adicionales * (valor_hora * 1.5)
            salario_bruto = salario_normal + salario_adicional
        else:
            salario_bruto = horas_trabajadas * valor_hora

        # Mostrar los resultados
        print(f"\nSalario bruto semanal: ${salario_bruto}")
        print(f"Horas adicionales trabajadas: {horas_adicionales}")

    except ValueError:
        print("Error: Por favor, ingresa números válidos.")

# Ejecutar la función
calcular_salario_mecanico()