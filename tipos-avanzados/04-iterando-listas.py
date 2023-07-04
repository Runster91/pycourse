# las listas  son iterables (strin, range) se pueden iterar con  for
mascotas = ["cookie", "Rocko", "Nina", "Canela"]

# for mascota in mascotas:
#     print(mascota)#es para  acceder al indice  del objeto que e stamos  iterando no  se puede hace  pero  podemos  pasarle mascotas a una funcion  que nos  devuelva un iterable
# enumerate) nos da  algo asi (0, 'cookie') esto es una  tupla
#  las tuplas pueden ser  accesadas igual  que  un listado 
for mascota in enumerate(mascotas):
    print(mascota)
# print(mascota[0]) nos  devuelve el primer  el emnto  de una  tupla)
#primero , segundo = [1, 2] asi como el  desempaquetar  es como  lo que  podemos  hacer con las  tuplas de  enumerate   ya que  es lo que nos  devuelve
#por cada  una  de  sus  iteraciones  con  for  print (mascota[1]) vamos  aoder  tomar el primer  elemento o indice   y el  segundo va  a ser el  numbre
#con for indice, mascota in enumerate(mascotas) >>> print(indice,mascota) nos mostrara el indice 0 cookie y el   elemento mismo que estamos iterando
