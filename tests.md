Documentacion de Pruebas - Calculadora Python

Descripcion del Proyecto Calculadora basica que implementa operaciones aritmeticas fundamentales con pruebas unitarias, de integracion y de rendimiento.

Pruebas Implementadas

Pruebas Unitarias

1.1 test_suma_positiva Tipo: Prueba unitaria Proposito: Verificar que la suma de numeros positivos funcione correctamente Entrada: 5, 3 Salida esperada: 8 Criterio de exito: resultado == 8

1.2 test_suma_negativa Tipo: Prueba unitaria Proposito: Verificar que la suma con numeros negativos funcione correctamente Entrada: -2, -3 Salida esperada: -5 Criterio de exito: resultado == -5

1.3 test_resta Tipo: Prueba unitaria Proposito: Verificar la operacion de resta basica Entrada: 10, 4 Salida esperada: 6 Criterio de exito: resultado == 6

1.4 test_multiplicacion Tipo: Prueba unitaria Proposito: Verificar la operacion de multiplicacion Entrada: 7, 6 Salida esperada: 42 Criterio de exito: resultado == 42

1.5 test_division Tipo: Prueba unitaria Proposito: Verificar la operacion de division normal Entrada: 15, 3 Salida esperada: 5 Criterio de exito: resultado == 5

1.6 test_division_por_cero Tipo: Prueba unitaria (caso limite) Proposito: Verificar que la division por cero lance una excepcion Entrada: 10, 0 Salida esperada: ValueError Criterio de exito: Se lanza ValueError

Pruebas de Integracion

2.1 test_operaciones_encadenadas Tipo: Prueba de integracion Proposito: Verificar que multiples operaciones funcionen correctamente en secuencia Entrada: [('suma', 10), ('resta', 3), ('multiplica', 2), ('divide', 2)] Salida esperada: 7 Criterio de exito: resultado == 7 Proceso: ((0+10)-3)*2/2 = 7

2.2 test_operaciones_complejas Tipo: Prueba de integracion Proposito: Verificar una secuencia compleja de operaciones matematicas Entrada: [('suma', 5), ('multiplica', 3), ('resta', 10), ('divide', 5)] Salida esperada: 1 Criterio de exito: resultado == 1 Proceso: (((0+5)*3)-10)/5 = 1

Pruebas de Rendimiento

3.1 test_rendimiento_suma_masiva Tipo: Prueba de rendimiento Proposito: Evaluar el comportamiento bajo carga pesada Escenario: Ejecutar 100,000 operaciones de suma consecutivas Metrica: Tiempo de ejecucion total Limite aceptable: Menos de 1 segundo Criterio de exito: tiempo_ejecucion < 1.0 segundos Objetivo: Garantizar que la calculadora pueda manejar grandes volumenes de operaciones eficientemente

Ejecucion de Pruebas

Para ejecutar todas las pruebas:

python test_calculadora.py