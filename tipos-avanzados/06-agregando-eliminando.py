mascotas = ["Nina",
            "cookie",
            "Rocko",
            "Nina",
            "Rocko",
            "Canela"]
# Para  eso  poemos   usar el metodo  de insert ,yle  decimos  el valor  donde  queremos  agregar el elemento
# seguido  del valor que queremos ingresar dentro  de e se  Indice
mascotas.insert(1, "Blackie")
mascotas.append("cochi triste")
print(mascotas)
# en caso  de querer  agregarlo  al  final  de mi listado se puede usar el  -1 pero es meor usar mascotas.append diciendole  cual e s el  elemnto que hay  que  agregar al final  de la  lista
# para eliminar  elementos  en un  listado usamos  .removeindicandole  cual  es  el  elemento que  queremos  eliminar
mascotas.remove("Rocko")
print(mascotas)
# si  hay   varias instancias que borrar  remove solo elimina  el primero y si  se queire  ver todas  hay  que  ver  cuatas   veces  se  repite  y   comenzar a  borrarlos
si  queremos  eliminar el ultimo usamos .pop
mascotas.pop()
# para  eliminar  un  elemento  en  particuelar se  establece c on el indice(1)
# tambien  se puede usando la  palabra del seguido  del listado al cualqueremos  quitar el elemento
del mascotas[0]
# para limpiar completamente e l areglo seria   con clear  mascotas.clear()
