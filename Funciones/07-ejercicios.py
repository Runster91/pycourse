# un palindormo es una  palabra  frase  u oracion que  se  escribe igual derecho o  al reves*Reconoocer=Reconocer)
# da falso opositivo  dependiendo  si es  palindromo o np
# def es_palindormo(texto):


# print("Abba", es_palindormo("Abba"))
# print("Reconocer", es_palindormo("Reconocer"))
# print("Amo la paloma", es_palindormo("Amo la paloma"))
# print("Hola Mundo", es_palindormo("Hola Mundo"))
# 1.-Necesitamos   una   funcion  que pueda eliminar  los   espacios en blanco de un string
# 2.-funcionque Tome un  texto>reverse(construir  este   reverse  aplicar  for  e  itrar  los  caracteres)
def no_space(texto):
    nuevo_texto = ""  # iterar i concatenar co cnada  uno  de los caracteres  de nuevo texto siempre y  cundo este  no se a un  string  vacio
    for char in texto:  # le  damos  char  porque e s un  cararcter
        if char != " ":  # aqui vamos  a concatenar  cada  un o  de los  caracteres  con  nuevo  texto
            nuevo_texto += char  # +=para concatenar un  string  con el otro  char y eso  va a i cocatenando  cada  uno  de  los  caracteres  a menos que  este  sea  un espacio en blanco

    return nuevo_texto
# un return fuera  del  for
# para la segunda parte  en la sugnda parte hay que  crear  una  vaiable  que  va  a contener  el  string   al reves


def reverse(texto):
    texto_al_reves = ""  # ahora  hay  que  iterar  en la  line  siguien  hay que  llamar  a for
    for char in texto:  # empezar  a  concatenar  los  caracteres  al  comienzo  en  vez  de  al  final
        # += ocncatena  a la  derecha y como lo queremos   ala izquierda,seia  la parte  depsues  del  igual  la  que leva dar la  vuelta  al   string
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_Palindormo(texto):
    texto = no_space(texto)
    texto_al_reves = reversed(texto)
    print(texto_al_reves)
    # Esto nos  devuelve  un  valor  boolean
    return texto.lower() == texto_al_reves()
# asi   se  crea  la  funcion de  reverse


print(es_Palindormo("amo la paloma"))  # true
print(es_Palindormo("Hola Mundo"))  # False
print(es_Palindormo("Reconocer"))
print(es_Palindormo("Somos o no somos"))