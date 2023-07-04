# lista = [1, 2, 3, 4]
# print(lista)
# sinosotros quisieramos  tener todos  estos  elemento slos  de  como
# lista = [1, 2, 3, 4]
# print =(1, 2, 3, 4)
# para  esto  debemos  llamar al operador del desempaquetamiento
# lista = [1, 2, 3, 4]
# print =(1, 2, 3, 4)
# print(*lista)
# esto sirve  para cuando tengamos una  funcion definida que  reciba   argumento sy  tenemos los  argumentos  dentro  de una lista
# lo que debemos  hacer es llamar a  esta  funcion pasandole lal ista pero  agreggamos el operador  de desmpaquetamiento(*) para  que se los pase cada uno como cada uno de sus  argumentos
# con el  operador  de desempaquetamiento lo que  tambien podemos  hcaer  es combinar  listas
lista1 = [1, 2, 3, 4]
lista2 = [5, 6]
# generaremos una  lista  combinada, tamben podemos  agregar  lementos  al comienzo
combinada = [*lista1, *lista2]
print(combinada)
# combinada = ["Hola", *lista1, "mundo", *lista2, "chanchito"]
# esto tambien  se puede  hace  con los  diccionarios  la diferencia  es que la sintaxis  va  a ser similar a esta en  ves  de un  asterisco va a usar  2
# print(combinada)

# operador  desempaquetamiento para los  diccionarios
punto1 = {"x": 19}
punto2 = {"y": 15}

nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)

# la froma  de asignar  la s  propiedades  es dela derecha  a la  izquierda
# punto1 = {"x": 19, "y": : "Hola"}
# punto2 = {"y": 15}
# si  agregamos  de nuevo la propiedad  de y si tenemo  dos  elemetos  x se va a  cmabiar  por el que  esta  en la derecha pero si esta x no esta en la  izquierda se va  a seguir  y  se va   asignar  al  diccionario qu esta en la  izquierda
# podemos  agregar  a este diccionario
# nuevoPunto = {**punto1, : **punto2, "z":"mundo"}
# print(nuevoPunto)
