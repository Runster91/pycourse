# si todas las  operaciones  dentro de  una  funcion  yo quisiera obtener  estos valores para luego  pasarleos  a otra  funcion o a  otro  print
def suma(a, b):
    resultado = a + b
    return (resultado)


# return  nos  va  apremitir  la variable  resultado y devolverla  cada vez que nosotros llamemos  a esta  funcion de  suma o cualquier otra  funcion
# creamos  una  nueva variable  c  la  cual  va  a devovler u nvalor y selo asigna a c
c = suma(1, 2)  # esto daria error pero la llamaremos en la siguiente
d = suma(c, 2)

print(d)
#esto toma  c y nos  da el valor  de  5

