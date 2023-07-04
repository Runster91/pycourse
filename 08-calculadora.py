n1 = input("ingresa primer  numero")
n2 = input("ingresa primer  numero")
n1 = int(n1)
n2 = int(n2)
print(n1 + n2)

suma = n1+n2
resta = n1-n2
multiplicacion = n1*n2
division = n1/n2

mensaje = f"""
Para los numeros {n1} y {n2}, el resultado de la suma es {suma}.
Para los numeros {n1} y {n2}, el resultado de la resta es {resta}.
Para los numeros {n1} y {n2}, el resultado de la multiplicacion  es {multiplicacion}.
Para los numeros {n1} y {n2}, el resultado de la division es {division}.

"""
print(mensaje)
