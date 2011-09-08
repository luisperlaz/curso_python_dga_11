# -*- coding: utf-8 -*-

'''
Created on 07/09/2011

@author: lm
'''

import csv

ORIGEN_DATOS = 'poblacion_2010.csv'
# 1. Analizar estructura fichero csv
# "Código","Municipio","Hombres","Mujeres"," Variación 2009-2010 "
PROVINCIAS={'huesca': '22',
            'zaragoza': '50',
            'teruel': '44'}


def listado_municipios(provincia):
    '''Muestra el nombre y población de los municipios de una provincia'''
    with open(ORIGEN_DATOS) as fin:
        reader = csv.reader(fin, delimiter=",")
        reader.next()  # quito cabecera
        for linea in reader:
            if len(linea) == 5 and \
                linea[0].startswith(PROVINCIAS.get(provincia, ' ')):
                print "%-25s  %9d" % (unicode(linea[1]), 
                                      int(linea[2].replace('.', '')) + \
                                      int(linea[3].replace('.', ''))
                                      )

def suma_poblacion(provincia):
    '''Muestra el nombre de la provincia y el total de la población'''
    with open(ORIGEN_DATOS) as fin:
        reader = csv.reader(fin, delimiter=",")
        reader.next()  # quito cabecera
        suma_pobl = 0
        for linea in reader:
            if len(linea) == 5 and \
                linea[0].startswith(PROVINCIAS.get(provincia, ' ')):
                suma_pobl += int(linea[2].replace('.', '')) + \
                             int(linea[3].replace('.', ''))
        print provincia.title(), suma_pobl




if __name__ == '__main__':
    listado_municipios('teruel')
    print '*' * 40
    suma_poblacion('zaragoza')
    