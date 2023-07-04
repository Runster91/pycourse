# iterar una lista  de  elementos principalmente
# ejemplo nombre + apellido =nombre  completo
# buscar elementos  y  operaciones  matematicas
# range   crea una  secuencia  de  numeros  del  0al 4
# numero  guarda  cada valor  del  range

# for numero in range(5):
#     print(numero, numero * 'hola mundo')

buscar = 10
for numero in range(5):
    if numero == buscar:
        print("encontrado", buscar)
        break
# si no se pone el break el ciclo  sigue
else:
    print("no encontre el  numero buscado ")
# iterables  son cualquier consa  con la cualpodamos  iterar en este e jemplo   seria el  5 o donde se guarde la variable
for usuario in usuaios:
    usuario.id
# en pyhton  hay muchos  iterables como listas y las  tuplas ,strings
for char in "Ultimate Python":
    print(char)
