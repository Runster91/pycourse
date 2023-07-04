# and (dos condiciones, con que uno sea false  se ra  false  el resultado), or(similar a andpero con que uno sea true  el resultado  sera  true, si ambos s on false seran  false), not (negar una operacion)
gas = True
encendido = True
edad = 18
# not  puede  cambiar  de  true  a false
if not gas or (encendido or edad > 17):
    print("Puedes avanzar")
# parapriorizar las  condiciones  se  necesita que  el parentesis  lo  seleccione
# operador  de  corto circuito   and  ambas  deben ser  true pero sil aprimera  es falsa   y loque  este  en  la  derecha  no lo va  a evaluar
# las operaciones  se  ejecutan de  izquierda  a  derecha  siempre
# or necesita  que  el  valor  de la  izquierda  sea  true  para  que no  se  evalue  el otro   pero si es  false  sise evalue  el  2do
