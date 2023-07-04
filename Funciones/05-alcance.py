# def saludar():
#     saludo = "Hola Mundo"
#     print(saludo)


# def saludaChanchito():
#     saludo = "Hola chanchito"


# # print(saludo) da name 'saludo' is not defined. Did you mean: 'saludar'? que dice que  esta  variable no existe  o no esta definida
# # cuando nosotrso  creamos un avaliable  solo  va  a servir  dentro  de la misma  funcion
# # no se puede  llamar  desde  afuera

# saludar()

# Si lo ponemos  especifico   podemos  llamar la  variable  con diferentes  contextos
# siponemos lavariable  aca   va a tener  un  contexto global es decir  que el alcancede la variable  puede ser accedida por todo  el codigo del archivo alcance.py

# saludo = "Hola Global"
saludo = 25


def saludar():
    # print(saludo)#da el error UnboundLocalError: local variable 'saludo' referenced before assignment ya  que python  pide primero  definir y despues  hacer  referencia  a ella
    # saludo = "Hola Mundo"
    saludo = "Hola Mundo"
    print(saludo)
    # cuando  hacemos  el print  jamas  traemos  el  contesxto global


def saludaChanchito():
    saludo = 24
    # saludo = "Hola Chanchito"
    print(saludo)


resultado1 = saludo + 3
print(resultado1)
# print(saludo)  # asi  ahora  sale  primero  global
saludar()  # python  sabe  que nos  referimos  a la  variable  que  esta en la  funcion saludar
resultado2 = saludo + 3

# saludaChanchito()
# saludar()
# python  sabe  que etsa trabajando  con la variable    de contexto  global
print(resultado2)
# print(saludo)
# variable  globales= mala practica no  usarle
# ya  que   al   cambiar   en la  segunda  funcion el string  por un numero   dejariade funcionar la  a poruq e es  un in  y no un  string  como la   global
# Las Variables  globales no se usan pero en  casi  de  querese  usar  seria  de la sig manera

# ///////////////////////
# def saludar():
#     global saludo  # asi  python ya sabe  que  es la  global
#     saludo = "Hola Mundo"
# ////////////////////////
