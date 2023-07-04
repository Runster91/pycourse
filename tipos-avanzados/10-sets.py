# conjunto o  grupo,  coleccion de  daots queno se puede repetir y  que tampoco esta ordenad
primer = {1, 1, 2, 2, 3, 4}
# primer.add(5)
# primer.remove(1)
# print(primer)
# da solamante una ocurrencia  de cada uno de estos  datosremueve  duplicados
# se elimino el  1  y se  agrego el  5
# vamos  a crear e l segundo  set el cual  sera  una  lista, transformar un alista  aun set
# vamos  areemplazar  nuestra variable  de segundo,sams  la funcion  set
# set  recibe un iterable
segundo = [3, 4, 5]
segundo = set(segundo)
print(segundo)
# operadores interesantes  que  tienen los sets
# tambien s epodria  hacer  nm base a una tupla
# print(primer | segundo)
# hizo  un   union  de los  sets que  le pasemos y elimina los elementos  duplicados
# el operador |(union) es  de union
# print(primer & segundo)
# nos devuelve  el  3  y  4  porque  &(interseccion) nos da los  elemoentos  que esten e n el  primer  set y en el s egundo  set
# print(primer - segundo)
# el  simbolo de  diferencia  es con el  de -(mostrar  sololos datos del conjnto  de izquierda  y le  quitamos los  que  estan en la derecha)
print(primer ^ segundo)
# diferecie  simetrica ^(carette) devolver a los  lementos  que  se encuentren  en el  primero  y el segundo  pero  que no se en encuentren en el  otro
#ademas sigue  eliminan duplicados
#los sets no son ordenados  y no se puede  acceder a un elemento  de estos  