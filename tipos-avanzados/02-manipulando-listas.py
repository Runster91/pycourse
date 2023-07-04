# mascotas = ["odie", "canela", "nina", "cookie"]
# podemos  acceder a cada elemento  usando [] cne l indice del elemento  al cual queremos  acceder
# print(mascotas)
# print(mascotas[0])
# para cambiar unelemento  del listado  lo haremosusando [0] accendiendo al   elementoy con el simbolo de igual le indicamos  cual sera  el  nuevo  valor
# mascotas[0] = "Rockinho"
# print(mascotas)
# print(mascotas[0:3])#[0:3]indica que nos  va  devolver  los primeros  elementos/ si no pongo  el primer  elemento [:3]python lo toma  por  defecto cero
#si yo  omito  el  valor  de la  derecha [2:] no s  va  a tomar la longitud  del  arreglo  o en en el  caso del ultimo elemento
# print(mascotas[-1])#menos  uno  a la  izauierda
# print(mascotas[::2])#le decimo  toma  el primer  elemento  ,  saltalo toma  el primer  elemento  ,  saltalo y  depues tomalo
# #si usamos[1::2] toma canela salta nina   y  acepta  cookie
# print(mascotas[1::2])
# print(mascotas[1:2:2])#Le indica  hasta cuanto  queremos  llegar de los elementos  a  seleccionar

numeros = list(range(21))
print(numeros)
print(numeros[::2])#devuelve los pares
print(numeros[1::2])#da los impares porque  le  decimos  de  donde  empezar
#para  emperarlo de otre manera  tambien seria  de la s iguiente  manera numeros = list(range(1, 21))