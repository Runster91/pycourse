# ejemplosimple
# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2


# comando = " "

# while comando != "salir":
#     comando = input("$ ")
#     print(comando)
# puede usare comando.lower para  que  sea  de  cualquier forma


# loopsinfinitos
comando = ""

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break


# loop  infinito es cuando  no hayuna  condicion de  salida y el while  se corre   de manera  infinita
# a los loops infinitos  siempre agregarle  un condicional de salida
