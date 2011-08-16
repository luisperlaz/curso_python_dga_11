# -*- coding: utf-8 -*-


"""
Media de las notas de un alumno

Necesita easygui
"""

from easygui import *

notas = []
while True:
    nota = enterbox('Introduce notas', 'Notas alumno')
    if not nota:
        break

    # detección fin de entrada: Cancel devuelve None. Salir de while con break

    # si había una nota: convertir e introducir en la lista



# calcula la media. Cuántas notas había?


# redondea


# Muestra mensaje

msgbox('La nota media es ...')
