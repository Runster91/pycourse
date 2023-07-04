
# parametros  a  key word a rguments  que es una manera  de e mpaquetar  todos los parametros  en un solo parametro
# k(key)w(word)args,cuando  trabajamos  con   kwargs  debemos  agregar  otro asterisco mas
def get_product(**datos):
    print(datos["id"], datos["name"])


# para poder  acceder alos  argumentes  desde  este parametro podemos acceder  a  esto  valores utilizando  el parentesis  cuadrado o corchete y  aho denro  colocamos  dos  comillas y  el  nombre  del id  del dato
# se llama a la  funcion  y  se pasanlos  argumentos  pero son  bajo  demanda
# tengo que avisarle  apython que  cada vez  que  este usando un  kwarg tengo que  indicarle  si o si  el  nombre  del  parametro
# rs/Guill/OneDrive/Desktop/proyx/cursopy/Funciones/03-kwargs.py
# {'id': 'id'} esto  es  un  diccionario
# cuando  nosotors  estamos  pasando una  funcion y le  est mos  dando asteriscos al parametro  necesaiament e tenemos que indicar  el  nombre  del  parametro que  se ha  asignado
# podemos  ponerle  todos los que  queramos get_product(id="id", name="iPhone", desc="Esto es un  iphone")
get_product(id="23",
            name="iphone",
            desc="Eso es un iphone")


