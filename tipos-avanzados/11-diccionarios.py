# los  diccionarios  son una  conexion de  datos que se  encuentran agrupados  por una llave y un  valor
# los  diccionarios  son  sumamente  usados  ya que es como las bases de datos nos  devuelven a nosotros los  datos
punto = {"x": 25, "y": 50}
# solamente acepta stirngs como la llave, lo de la izquierda es un s tring  y lo de la derecha  es cualquier  cosa
# para  diccion ario se usa el curly  bracket  y  cada  llave  se  va  a definir  con un  string, si hay  mans de una llave  separar con comas
# cuando  queremos  acceder  a uno de losvalores de estas  llaves podemos usar el parentesis cuadrado
# no son  listas ni sets asi que no se puede acceder a estos  valores utilizando  0 o 1
# debemos idicarle mediante un string  cual es la llave a la  cual queremos acceder
print(punto["y"])
print(punto["x"])
# tambien podemos  agregarle  mas  llaves  al  diccionario bajo  demanda
punto["z"] = 45
print(punto)
# si queremos  acceder  a una llave  que no existe hay que  verificar si existe o no con un if
# print(punto, punto["lala"])
if "lala" in punto:
    print("encontre lala", punto["lala"])
# el siguiente  metodo  quepodemos usa para accedera unvalor del  diccionario  pero  que nuestra  app no epxlote  es uar el  get  de  diccionarios usaremos  get
#  indicando el striong  como argumento  la  cual  es la  llave
print(punto.get("x"))
# cuando la  llave no existe devuelve none, tambien podemos  pasarle  un  valor  por  defecto en caso d e que la llave no exista  y eso  se pasa  como segundo  argumento
print(punto.get("lala", 97))
# si quisiera  eliminar una  de estas  llaves incluyendo su  valo  usando   del  siguiendo el  nombre del valor
del punto["x"]
print(punto)
# agregamos  denuevo el valor  de  x
punto["x"] = 25
# si  yo quiero  iterar  todas  las  llaver  consu valor  yo puedo hacer eso  con un for
# for valor in punto:
#     print(valor)
# imprime  z y  x  que son las llaves  que  tiene  asociado este diccionario
# si quisiera  acceder  alos  valores  debo llamar a mi diccionario y pasarle el  valor con  parentesis  cuadrados
for valor in punto:
    print(valor, punto[valor])
# tambien podemos usar  esta  otra llmando  al  metodo   itemse imprimiremos  valor
for valor in punto.items():
    print(valor)
# nos devuelve tupla  y como fue  aprendido podemos  hacer un desempaquetado  de las  tuplas para poder a cceder a sus valores al ugual  que las  listas
#  for llave, valor in punto.items():
#     print(llave, valor)

  #ejemplo real  de uso d e diccionarios
#cuando trbajamos con elementos que  vienen  de una base de  datos necesariamente  debemos  tener un  identificador  unico 
#a este  identificador lo conoceremos  como  id
usuarios  = [{"id": 1, "nombre" : "Chanchito"}
    {"id": 2, "nombre" : "Feliz"}
    {"id": 3, "nombre" : "Runster"}
    {"id": 4, "nombre" : "bebe"}
    ]
#si quisieramos  acceder  a los nombres tendriamos  que iterar lso usuarios 
for usuario  in usuarios:
    print(usuario["nombre"])