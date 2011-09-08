# -*- coding: utf-8 -*-

'''
Crea nombre de usuario.

Nuestro programa pide el nombre y el apellido de un usuario. Imprime en
pantalla en nombre de usuario creado: inicial del nombre, guión bajo y
apellido.

VARIACIÓN:
* sólo se usarán letras sin acentos (ascii)
AYUDA:
    Usa el módulo unicode data http://docs.python.org/library/unicodedata.html:
    > import unicodedata
    > unicodedata.normalize("NFD", u'á')[0]
    u'a'
    > unicodedata.normalize("NFD", u'ñ')[0]
    u'n'
'''


def crea_nombre_usuario(nombre, apellido):
    '''
    Devuelve nombre de usuario formado por inicial de nombre y apellido,
    separadas por guión bajo.

    >>> crea_nombre_usuario('Luis', 'Malo')
    'l_malo'
    '''
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
