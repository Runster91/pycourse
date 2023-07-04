numeros = [2, 4, 1, 45, 75, 22]

# numeros.sort(reverse=True)
# para ordenarlo  pero al  reves hay  que  ponerle  un argumento al parentesis  de  sort en este  caso reverse
# otrometodo es el  de  sorted y hay  que pasarle  el iterable  que queremos  ordenar
# la diferencia en tre sorted(devuelva una  nueva lista, no afecta el anterior) y el metodo  de sort (ordena  el areglo)
# numeros2 = sorted(numeros)
# print(numeros)
# print(numeros2)
# si quisieramos  cambiar  el  orden en  sorted  debemos  darle  un  reverse
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)
# si queremos  oredenar  algo mas  complejo ejemplo  un listado  con  listas a dentro
# usuarios = [[4, "Chanchito"],
#             [1, "Felipe"],
#             [5, "Pulga"]]
# usuarios.sort()
# print(usuarios)
# si l e damos  el   id   al  final ,no lo va  a  ordenar   , siempre  y cuando  el iterable  sea  algo ordenable si lo ordenara
# #tuplas  se colocan  con los  parentesis
# parapoder lograrlo de esta  maner  utilizaremos   la  funcion  ordena y  le  especificamos  el elemento por le cual vamos a ordenar
# a sort  le pasamos  el moetodo  ordena
usuarios = [["Chanchito", 4],
            ["Felipe", 1],
            ["Pulga", 5]]


# def ordena(elemento):
#     return elemento[1]


# usuarios.sort(ordena)
# no esta  tomando ningun elemento para   eso  debemos indicarle  el parametro
# usuarios.sort(key = ordena)
# de esta manera  ya  esta   ordenado
# si  queremos  que sea  al   reves  debemos  pasarle  otro  argumento   en este  caso  va  a ser un reverse
# usuarios.sort(key=ordena, reverse=True)
# la funcion  hacer   que  pormedio  de key  a ordena yle  de  elemento  cada  que   lo necesite
# print(usuarios)

# ///tuplas  funciones Lambda  o funciones anonimas

# para hacerlo  mas  elegante  debemos   escribir  lamba  acontinuacion de los  parametros  que  recibe la funcion  y seguido  de  eso el contenido de la funcion en este  caso sera  el  calor  de  retorno

usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
# al usar lambda  nos  ahorramos  lapalabra  de def,  el  darle nombre  a la  funcion, tener   que  pasarle  los   parentesis  ademas nos  ahorramos  el pasarle  return
# usar solamente  funciones lambda pero   cuando  solo se  va  a usar una esta bien , en este  caso lambda  accede  al segundo e lemento  de un listado de  esta  forma  podriamos ya no  necesitar  de la funcon
