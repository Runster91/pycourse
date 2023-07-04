def largo(texto):
    resultado = 0
    for _ in texto:
      #   for char  in texto:
        resultado += 1
    return resultado
# Me marca  error  por que  char no lo estoy utilizando netonce s  lo cambiio  por _ para  quitar  el warning  en nuestro  codigo


print("chanchito")
l = largo("Hola Mundo")
print(l)  # nos muestra  solo 1  en lugar  de todo el legnht  que  tiene  Hola Mundo(10)
# para  hacer  el  runand  Debug  primero  debemos  crear  un  json file y vscode  va a poder utilizar  ese  archivo  par a poder  depurar nuestro codigo
# seleccionamos  python y   la buscamos  podremos  darnos  cuenta  que tenemos  una  carpeta llamada vs code  y vemos  un  archivo llamado  launch.json
# y regresamos a nuestro archivo para correr el depurador
# alparece no apsaa  nada   pero es porque  tenemos  que  darle  un punto donde  el depurador  se va a  detener y cuando  se  detenga  podemos  empezar  a analizar  nuestra  app
# ponemos  el punto  a  un lado  del numero  , a esto lo conocemos  como break point en una linea  aprticular y hace  que  el  depurador  se detenga
# despues  vamos  a  function variables,  ahi vemos  que esta  definida  la funcion  de largo
# tenemos  que  avanzar  para  eso  tenemos  qu epicarle al punto con la   flecha  hacia a dleante conocido como step overo  f10, mac  es  function  y  f10
# ya nos   hizo  avanzar  una linea si no  sale nada  avanzamos  una linea  mas al  hacr  esto no ingrso  a revisar la funcion del   renglon anterior
# ahora me sale l y  largo , damos  un salto mas   y termina  depuracion
# lo correremos de nuevo  y   vamos a la linea 9 y  l e picamos al punto ocn flecha  hacia  abajo  llamado como step into ejecutado ocn f11 en mac es fn +f11
#  eso  nos me te  ala  funcion   y nos muestra  el  hola  mundo  en  la izquierda  de nuevo  step  over
# nos  da mayor informacion nos  dice  de  _ H que  seria  la primera letra  que nos da  el vlaor de 1 dmos  step over
# nos pmanda  aprint  comono  es lo que  queremos  le damos  acuadro para  detener el debugger
# quitamos la  identacion del  return y  guardamos
# ejecutamos  de nuevo el debugger
# damos  step  over,step into
# nos da  variable  de texto damos  step  over  y  vemos  que  ya  esta  la  variable  de resultado
# damos  step  over step into  step  tintp  un poco  de  step over  y vemnos  como ya  esta  funcionando   damos   step out  shift  f11 mac  es  fn  shift  y  f11
# si  reiniciamos   sale   ponemos  brak point en la linea  12 y   vemos  que sale  un   boton de play  que nos llava de la  10  a la 12
# detenemos  depurador   shift + f5
# en este  caso  retunr   estaba  regresando  uno  ya   que al  estar  identado   seguia  regresando  el mismo  valor  de la l inea  anterior
