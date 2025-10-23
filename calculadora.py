def calculadora_basica():
    print("=== CALCULADORA BÁSICA ===")
    print("Operaciones disponibles:")
    print("+ : Suma")
    print("- : Resta")
    print("* : Multiplicación")
    print("/ : División")
    print("q : Salir")

    resultado = None  

    while True:
        try:
            if resultado is None:
                num1 = float(input("\nIngrese el primer número: "))
            else:
                print(f"\nResultado anterior: {resultado}")
                usar_resultado = input("¿Desea usarlo como primer número? (s/n): ").lower()
                if usar_resultado == 's':
                    num1 = resultado
                else:
                    num1 = float(input("Ingrese el primer número: "))

            operador = input("Ingrese el operador (+, -, *, / o q para salir): ")
            if operador.lower() == 'q':
                print("¡Hasta luego!")
                break

            num2 = float(input("Ingrese el segundo número: "))

            if operador == '+':
                resultado = num1 + num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
            elif operador == '/':
                if num2 == 0:
                    print("Error: No se puede dividir entre cero")
                    continue
                resultado = num1 / num2
            else:
                print("Operador no válido")
                continue

            print(f"Resultado: {num1} {operador} {num2} = {resultado}")

        except ValueError:
            print("Error: Por favor ingrese números válidos")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break

calculadora_basica()
