def menu(): 
    print("Bienvenido a LógicaBin")
    print("1. Simular puerta lógica")
    print("2. Generar tabla de verdad")
    print("3. Resolver expresión booleana simple")
    print("4. Salir")
    return input("Seleccione una opción: ")

def puerta_logica(a, b, tipo):
    if tipo == "AND":
        return a & b
    elif tipo == "OR":
        return a | b
    elif tipo == "XOR":
        return a ^ b
    elif tipo == "NAND":
        return int(not (a & b))
    elif tipo == "NOR":
        return int(not (a | b))
    else:
        return None

def simular_puerta():
    print("\nSeleccione la puerta lógica: AND, OR, XOR, NAND, NOR, NOT")
    tipo = input("Tipo: ").upper()
    if tipo == "NOT":
        a = int(input("Ingrese un valor (0 o 1): "))
        resultado = int(not a)
        print(f"Resultado de NOT {a} = {resultado}")
    else:
        a = int(input("Ingrese el primer valor (0 o 1): "))
        b = int(input("Ingrese el segundo valor (0 o 1): "))
        resultado = puerta_logica(a, b, tipo)
        if resultado is not None:
            print(f"Resultado de {a} {tipo} {b} = {resultado}")
        else:
            print("Tipo de puerta no válido.")

def tabla_verdad():
    print("\nTabla de verdad de A y B con AND, OR, XOR")
    print("A B | AND OR XOR")
    for a in [0, 1]:
        for b in [0, 1]:
            print(f"{a} {b} |  {a & b}   {a | b}   {a ^ b}")

def resolver_expresion():
    print("\nResolver: A AND (NOT B)")
    a = int(input("Ingrese A (0 o 1): "))
    b = int(input("Ingrese B (0 o 1): "))
    resultado = a & (not b)
    print(f"Resultado de {a} AND (NOT {b}) = {int(resultado)}")

while True:
    opcion = menu()
    if opcion == "1":
        simular_puerta()
    elif opcion == "2":
        tabla_verdad()
    elif opcion == "3":
        resolver_expresion()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")