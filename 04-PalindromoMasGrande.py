#-*- coding: utf8 -*-
#Programa: 04-palindromo
#Objetivo:Un Numero Palindromo es aquel numero que se lee igual, de izquierda a derecha y viceversa
          #El palindromo mas grande que se pued obtener por el producto de dos numeos de dos digitos 
          # es: 9009 que es igual a 91x99.
          #Encuentre el palindromo mas grande que se pueda encontrar por el producto de numeo de tres digitos.

          #Recomendacion: tratar de hacerlo con el ejemplo siempre.
#Autor: Fernando Martinez
#Fecha: 28 enero de 2020

def obtener_palindromo(valor):
    """
     Funcion que verifica si un numero es palindromo
    
    """
   
    #Luego de convertirlo a str, los vamos a insertar en una lista para luego verificar
    palindromo = list(str(valor))
    #lo insertamos en una nueva lista
    palindromo_final = palindromo
    
    #Luego aplicaremos la verificacion para comprobar si es un palindromo
    if palindromo [:: -1] == palindromo_final:
        return True


        
        #print('El numero es un palindromo')

def multiplicaciones(): #906609 tiene que darme
    """
    Funcion se encargara de crear las multiplicaciones entre 999 y 100

    mediante dos ciclos for.
    """
    ultimo_palindromo = 0
    total = 0
    for primer_numero in range(100, 1000):
        for segundo_numero in range(100, 1000):
            #total se encarga de hacer la multiplicacion entre los numeros
            total = primer_numero * segundo_numero
            # llamamos a la funcion que verifica si la multiplicacion que envia es un palindromo
            if  obtener_palindromo(total):
                #luego de verificar que la multiplicacion era palindromo pasamos a evaluarla hasta llegar al ultimo palindromo
                #entre 100 y 1000
                if  ultimo_palindromo < total:
                    ultimo_palindromo = total
    return ultimo_palindromo

#Llamamos a la funcion

if __name__ == "__main__":
    print(multiplicaciones())






