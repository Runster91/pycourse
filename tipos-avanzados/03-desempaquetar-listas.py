# numeros =[1, 2, 3]
# si queremos  desempaque  tarm  prumero cramos  una  variable
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]
# esto e s  feo  pero  se puede  hacer   de  la  siguiente  manera

# primero, segundo,  tercero = numeros
# print(primero, segundo, tercero)#esto es  mas  bonito
# para  desempaquetar  solo uno  vamos  a  hacerlo asi primero, *otros = numeros
# primero, *otros = numeros
# print(primero)
# el asterisco toma todos los  elementos  para meterlos  al parametro para  depues poderlos  iterar usando un  for
# es  decir  se empaquetanm en una  lista
primero, *otros = numeros
print(primero, otros)  # toma  el uno y lo saca
# Para  acceder al segundo  elemento

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo,  *otros = numeros
print(primero, segundo,  otros)
#si se necesitara el  primer y ultimo
print(primero, ultimo, otros)
primero, segundo, *otros, penu, ultimo = numeros #con  *se  guarda
print(segundo, penu, otros)