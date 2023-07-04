# las  funciones  son importantes  porque  salvan la necesidad   de  poner  exceso  de codigo
# print("Hola  mundo")  # imprime
# para crear  nuestra  propia funcion hay  que e scrbir  def, nombre  de la  funcion parentesis y  dos puntos y  debajo  poner  el  contenido de la funcion identado

# def hola():
#     print("Hola mundo!")
#     print("Ultimate Python")
#     # hay  que  volver a llamar a la funcion para que se pueda ejecutar
#     # Cuando  tenemos  activado Pep8   hace bonito  el codigo bajando  lineas

# hola()
# debemos  agrgarla vairables  en el  contexto de la funcion
# def hola():
#     print("Hola mundo!")
#     print("Bienvenido Runster")


# hola()

# debemos  agrgarla vairables  en el  contexto de la funcion
# def hola(nombre):
#     print("Hola mundo!")
#     print(f"Bienvenido {nombre}")


# hola("Runster")
# hola("Bebes contentos")

# cad vez  que se hace  referencia  auna variable  en una  funcion hacemos uso  de sus parametros en este caso nombre e s  un parametro
# al llamar  la  funcion y darle un valor  se lellaman  argumentos  en  este  ejemplo al volver a  llamarla  y darle  otro  valor hay  que agregar otro parametro
# en  este  ejemplo al  agregarle  un nuevo  parametro  seria  de  esta  forma def hola(nombre, apellido)
# como es mostrado  en  el  siguiente  ejemplo spearandolos por una coma como si fueran  un   nuevo string

# def hola(nombre, apellido):#parametros
#     print("Hola mundo!")
#     print(f"Bienvenido {nombre} {apellido}")


# hola("Runster", "Casillas")
# hola("Bebes contentos", "Abril")#Argumentos

# /////Argumentos  opcionales
# para que este use paremtros de manera opcional.Para  que esta  funcion utilize un  valor  por  defecto
# colocar un = ala derecha del parametro y con comillas  vamos  a indicarle cual es el  valor  que le pondremos por defecto
# pero si le damos un valor como en la llamada de  funcion  no tomara el  valor  opr defecto
def hola(nombre, apellido="Dinosaury"):  # parametros
    print("Hola mundo!")
    print(f"Bienvenido {nombre} {apellido}")


# hola("Runster", "Casillas")
# hola("Bebes contentos")  # Argumentos

#///////Argumentos  nombrados
#cuando  nosabemos  en  que orden  pasarle  el nombre y el apellido podemos  hacer  funcionar  esta  ejecucion de cualquier manera 
#si le  asignamos un nombre al argumento que  le estamos pasando haciendole saber a python que Casillas es el apellido y Runster  es el nombre
#se hace   en el inicio  poniendo apellido=schurman   y hay  que nombrar  todo nombre=Runster
hola (apellido="Casillas", nombre="Runster")


