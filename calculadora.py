def calculadora_basica():
    print("=== CALCULADORA BÁSICA ===")
    print("Operaciones disponibles:")
    print("+ : Suma")
    print("- : Resta")
    print("* : Multiplicación")
    print("/ : División")
    print("q : Salir")
    
    while True:
        try:
            num1 = float(input("\nIngrese el primer número: "))
            operador = input("Ingrese el operador (+, -, *, /): ")
            
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