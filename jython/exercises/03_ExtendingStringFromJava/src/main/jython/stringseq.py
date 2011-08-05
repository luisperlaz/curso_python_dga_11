'''
Created on Jul 27, 2011

@author: Luis Perez

Ejercicio creado con el proposito de mostrar la capacidad de extender una clase Java
(En este caso, java.lang.String), para que adquiera caracteristicas de python, pero en este
caso se hara desde Java. El unico codigo jython permitido son estos tests.

Ayuda:
    Dado que java.lang.String es final, se necesitara hacer una clase java wrapper que delegue
    en String, a la cual se agregaran los metodos necesarios para cumplir con los tests.
    
    Necesario implementar en los metodos __len__, __contains__, y __getitem__
    Ver (http://docs.python.org/reference/datamodel.html)
'''
import unittest

from es.neodoo.pythoncourse.extstring import ExtendedString

class Test(unittest.TestCase):
    
    def testStringLen(self):
        """testear que len(ExtendedString("string of size 17") funciona y devuelve 17"""
        s = ExtendedString("string of size 17")
        assert len(s) == 17
    
    def testStringIn(self):
        """testear que la sintaxis "A" in ExtendedString("ABC") funciona"""
        s = ExtendedString("ABC")
        assert "A" in s
        assert "N" not in s
    
    def testStringSubscriptable(self):
        """Testear que la sintaxis con indices ExtendedString("ABCDEFG")[3] es valida"""
        s = ExtendedString("ABCDEFG")
        assert s[0] == "A"
        assert s[1] == "B"
        assert s[6] == "G"
        assert s[-1] == "G"
        
    def testStringIndexOutOfBounds(self):
        """Testear que usar un indice mayor que la longitud de la cadena levanta un IndexError"""
        s = ExtendedString("ABC")
        try:
            s[5]
            self.fail("IndexError should've been raised")

        except IndexError:
            pass
        
    def testStringIndexTypeError(self):
        """Testear que pasar algo que no sea entero o slice como indice levanta una TypeError"""
        s = ExtendedString("ABC")
        try:
            s['asda']
            self.fail("TypeError should've been raised")
        except TypeError:
            pass
        
    def testStringSlice(self):
        """testear que se pueden usar slices como ExtendedString("ABCDEF")[2:4]"""
        s = ExtendedString("ABCDEFG")
        assert s[2:4] == "CD"
        
    def testStringReverse(self):
        """testear que se puede usar reversed(s) para revertir el orden de los caracteres"""
        s = ExtendedString("ABCDEFG")
        self.assertEquals(''.join(reversed(s)), "GFEDCBA")
        

if __name__ == "__main__":
    unittest.main()