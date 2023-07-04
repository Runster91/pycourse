print("Bineveidos  a la  calculadora")
print("Para  salir   escribe  salir")
print("las  operaciones  son  suma, resta, multi y div")

Resultado = ""

while True:
    if not Resultado:
        Resultado = input("Ingrese numero: ")
        if Resultado.lower() == "salir":
            break
        Resultado = int(Resultado)
    op = input("Ingresa operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        Resultado += n2

    elif op.lower() == "resta":
        Resultado -= n2
    elif op.lower() == "multi":
        Resultado *= n2
    elif op.lower() == "div":
        Resultado /= n2
    else:
        print("Operacion no valida")
        break
    print(f"El resultado es {Resultado}")
