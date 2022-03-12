# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:37:29 2022

@author: pekit
"""

# Advertencia: 
# No introduzcas ñ.

from typing import List

import math

def transforma_numero(caracter: str)-> int:
    """
    Transforma el digito alfabetico o numérico de str a un
    entero entre el 0 y el 35 (a es 10, b es 11... etc).

    Parameters
    ----------
    caracter : str
        Caracter del 0 al z con el que comienza la función.

    Returns
    -------
    int
        Número del 0 al 35 en el que se transforma.

    """
    caracteres: List = ["a", "b", "c", "d", "e", "f", "g", "h",\
                        "i", "j", "k", "l", "m", "n", "o", "p",\
                        "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if caracter <= "9" and caracter >= "0":
        digito: int = int(caracter)
    else:
        digito: int = 10 + caracteres.index(caracter)
    return digito


def main():
    """
    Introduce un código alfa-numérico y devuelve un valor decimal.

    Returns
    -------
    Pinta el valordecimal del código alfa-numérico

    """
    codigo: str = input("Introduce el codigo (no introduzcas ñ).: ")
    indice: int = 0
    numero: int = 0
    for indice in range (0, len(codigo)):
        numero += transforma_numero(codigo[indice])*36**(len(codigo)-1-indice)
        indice += 1
    print ("\n")
    print ("Es el numero ", numero)
    print ("Dicho número tiene", math.floor(math.log10(numero)) ,"cifras.")

if __name__ == '__main__':
    main()
