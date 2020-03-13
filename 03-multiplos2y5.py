#_coding_
# Programa: multiplos funcina
#Objetivo: Realizar funciones productivas con python 
#Autor: fernandomartinez
# Fecha: 1/enero/2020


def suma_multiplos_cinco_o_tres():
    '''
    Retorna la suma de todos los multiplos de 3 o 5 
    hasta un numero dado.

    parametros:
    valor: el valor del numero limite para calculo.

    '''
    suma = 0 
    for i in range(valor):
       if i % 3 == 0 or i % 5 == 0:
           suma += i

    return suma 

print(suma_multiplos_cinco_o_tres(1000))

