# este  tipo de  datos ,son una lista   se pueden  agregar numeros  caractere s  sublistas y juntarlas
numeros = [1, 2, 3]
letras = ["a", "b", "c"]
palabras = ["chanchito", "feliz"]
palabrasFelices = ["chanchito", "feliz", "alumno"]
print(palabras)
print(palabrasFelices)
booleans = [True, False, True, True]
print(booleans)
# una matriz  es un listado  que  contiene mas  listados
matriz = [[0, 1], [1, 0]]
print(matriz)
# de e sta  forma  se multipica  el  contenido y lo pone  10 veces
ceros = [0, 5] * 10
print(ceros)
# de esta manera  juntamos  2 listas en una  gran  lista
alfanumerico = numeros + letras
print(alfanumerico)
# para crear  un listado  con un  rango  de  numeros usamos  rango
# aqui en el parentesis debe  ser un  iterable sino le pasamos  nada  crea una lista vacia
# range = list(range(10))#dalistado con  10 elementos
range = list(range(1, 11))  # aqui le indicamos hasta  donde vamos a llegar
print(range)
char = list("hola mundo")
print(char)
# print(numeros)
# marca inicio  y  fin  de la lista
# el corchete   tambien  se usa  para  cceder  alos  indices  de un  string  "holamundo"[2] indicando  que  queremos ir  al indice 2 osea caracter  l
