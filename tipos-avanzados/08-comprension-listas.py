# de este  listado   vamos  a  querer  solo  el  nombre porque el identificador  no interesa
# vamos a  aplicarle  una  transformacion para quen os devuelva  una lista  de nombres, asi que pasaremos  de un listado  de usuario  auno  de nombres
# con   for  se podria  iterar crar unavariable   y conappend   agregar  cada un o de estos   nombres
usuarios = [["Chanchito", 4],
            ["Felipe", 1],
            ["Pulga", 5]]

# nombres = []  # lista vacia
# for usuario in usuarios:
#     nombres.append(usuario[0])  # 0porque vamos  a  sacar el   primer elemento
# print(nombres)
# funciona aunque  hay una  formammas  elegante  de  hacerlo y en una  sola linea
# vamos  a  crear una  nueva  lista y  le  vamos  a  decir como queremos  crear esta nueva  lista
# nombres = [expresion for item in items ]
# le indicamos la lista que estamos  iterando(item) despues elnombre que le vamos  a dar cada  elemento y  finialmente la expresion  que nosotros  le vamo s  a aplicar o la  transofrmacion que le  vamos  a aplicar a  este  elemnto  para  que  sea  asignado a la lista  de nobres
# se le pone  0 poruqe lo que  queremos  es el primer  elemento
# nombres = [usuario[0] for usuario in usuarios]*esta op[eracion  tambien se le conoce  ocn el  nombre  de map
# print(nombres)
# de  esta manera podemos  tomar una lista   y le  podemos  aplicar  una  transformacion a  cada uno  de los  elementos
# ahora  en lugar  de  transformarlo  vamos  a  filtrarlo y  en la  expresion hay que  colocarle  una  condicion a los elementos queme  va a a devolver

# nombres = [usuario for usuario in usuarios if usuario[1] > 2]*tambien  conocida como filter
# print(nombres)

# podemos  modificar una  lista  y filtrarle  al mismo  tiempo, aplicando  las   dos  operaciones
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
# de esta forma  fue  filtrada  y transformada

# print(nombres)
# lepasamos una funcion y el  valor a  retornar y  depues  incidcar  que  queremos iterar
nombres = list(map(lambda usuario: usuario[0], usuarios))
# deberiamos  ver los mismo  que con la s compresniones de listas
# Haremos lo mismo pero  con filter, filter  recibre  lamba  y esta si evalua en true va  a devolver  el elemento pero si  evalua en false no va  a dvolver el elemento
# seguido  de eso  tenemos  que indicarle  cual  es  la aista  que  tiene  que  iterar
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2), usuarios)
# de esta manera hacemos l mismo  de anter  pero  con   listas  de comprension
print(menosUsuarios)
