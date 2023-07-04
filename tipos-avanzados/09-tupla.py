# una tupla es lo mismo  que una  lista pero  diferencia en que no se puede modificar, pero  puedes crear nuevas listas o tuplas ne base  alas  ya existentes
# se puede concatenar  dos  tuplas para crear una  nueva tupla
# las  tuplas  se van a  usa  cuando no queramos modifcar  de manera accidental el contenido  dentro  de algun listado
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# para  transformar un listado  en una  tupla se  hace  de la siguiente manera,  la funcion de  tuple  recibe  cualquier cosa  que  sea iterable
# tambien puede pasarsele un string
punto = tuple([1, 2])
print(punto)
# conlas  tuplas se pueden hacer todas las operaciones que nosotros podemos  realizar  con las  listas excpecion de  aquellas   que permiten modificar las listas  ejemplo append o pop
# lo que  sipodemos  es  acceder  al contenido de la  tupla
menosNumeros = numeros[:2]
# esta operacion no modifica numeros  si no lo que hace  es que nos crea una nueva  lista la cualpodemos asignar a menosNumeros
print(menosNumeros)
# tambien podemos  desmpaquetar las tuplas
primero, segundo, *otros = numeros
print(primero, segundo, *otros)
# esto ya no me esta  dando una tupla sino una  lista
# tambien podemos  iterar las tuplas
for n in numeros:
    print(n)
# esto imprime  todos los  elementos  de  la  tupla
# si intentamos  modificarla se marca en  rojo y no permite
# numeros [0] = 5
# lounico   modificable  son  las  listas  no las tuplas  pero en caso d e ser necesario queno se recomienda
# es  crear una nuva  variable
listanumeros = list(numeros)
listanumeros[0] = "Chanchito Feliz"
print(listanumeros)
# aqui  mo dificamos  el  e lemtno  peor no modificamos la  tupla,  lo que  hicimo s de  crear  una  lista  en base  al a tupla  y modificamos  la  lista no la  tupla
