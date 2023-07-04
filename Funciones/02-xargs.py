# def suma(a, b):
#     print(a + b)


# suma(2, 5)  # son  iterables
# suma (2, 5 , 7)#como  todo  iterable  se le puede  aplicar  un for de esta manera  vamos  a recorrer todos  los numeros  que  se ncuentran dentro  delos  argumentos  de  una funcion

# suma(2, 8, 7, 45, 32)
# este nos va  aprmitir  tomar   todos los  argumentos que queramos
# * al comienzo  le  decimos  que se  trata de iterar

# el  print  debe  quedar  al nivel  del  for  para  que  este  funcione
def suma(*numeros): #* transforma  parametros en iterables
    resultado = 0
    for numero in numeros:
        resultado += numero

    print(resultado)


# se quda este  espacio par  dejar identacion  silo dejo el cilco se va  a raptir tantas  veces omo  elementos yo  le  deje  por eso  elimnamos  esa  lina para queno  siga  con ello como instruccion
suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)


 