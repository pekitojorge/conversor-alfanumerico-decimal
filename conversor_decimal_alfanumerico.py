# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 01:03:39 2022

@author: pekit
"""

# 825022

from typing import List

def transforma_codigo(digito: int)-> str:
    """
    Transforma un dígito decimal en un caracter alfanumérico.

    Parameters
    ----------
    digito : int
        Dígito decimal que se le pasa.

    Returns
    -------
    str
        Dígito alfanumérico que recibe.

    """

    caracteres: List = ["a", "b", "c", "d", "e", "f", "g", "h",\
                        "i", "j", "k", "l", "m", "n", "o", "p",\
                        "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if digito >=0 and digito <= 9:
        caracter: str = str(digito)
    else:
        caracter: str = caracteres[digito-10]
    return caracter

def main():
    """
    Introduces un número decimal y te devuelve un código alfanumérico.

    Returns
    -------
    Pinta el código alfanumérico.

    """

    numero: int = int(input("Introduce un numero: "))
    resto: int = 0
    codigo: str =""
    while numero != 0:
        resto = numero%36
        numero = numero//36
        codigo = transforma_codigo(resto) + codigo
    print ("El código es", codigo)
    print ("El código tiene", len(codigo) ,"caracteres.")

if __name__ == '__main__':
    main()
