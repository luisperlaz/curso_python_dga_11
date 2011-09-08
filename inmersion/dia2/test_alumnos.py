# -*- coding: utf-8 -*-


from nose import with_setup
from alumnos import Alumno

alumno = None  # crea referencia

def inicializar():
    print "setup"
    global alumno
    alumno = Alumno()
    alumno.nombre = 'Pedro'


def test_nombre():
    alumno = Alumno()
    alumno.nombre = 'Pedro'
    assert alumno.nombre == 'Pedro'
    assert alumno.apellido = 'Martínez'

@with_setup(inicializar)
def test_str():
    alumno.__str__() == u'Pedro Martínez'

