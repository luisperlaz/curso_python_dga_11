'''
Created on Jul 27, 2011

@author: Luis Perez

Ejercicio creado con el proposito de mostrar la capacidad de extender una clase Java
(En este caso, java.lang.String), para que adquiera caracteristicas de python.

Extenderemos la clase String para que adquiera capacidades como subscripting (ej: String("ABC")[3])
ver los tests vacios o por completar mas abajo.

Ayuda:
    Necesario implementar en java.lang.String los metodos __len__, __contains__, y __getitem__
    Ver (http://docs.python.org/reference/datamodel.html)
'''
import unittest

from java.lang import String #@UnresolvedImport
from java.lang import StringIndexOutOfBoundsException #@UnresolvedImport

def __string_length(self):
    return self.length()

def __string_contains(self, item):
    return self.contains(item)

def __string_getitem_index(self, key):
    if key < 0:
        key = len(self) + key
    try:
        return self.charAt(key)
    except StringIndexOutOfBoundsException:
        raise IndexError("Index out of range: %d" % key)

def __string_getitem_slice(self, key):
    start, stop, _ = key.indices(len(self))
    res = self.substring(start, stop)
    return String(res)

def __string_getitem(self, key):
    if isinstance(key, int):
        return __string_getitem_index(self, key)
    
    elif isinstance(key, slice):
        return __string_getitem_slice(self, key)
    else:
        raise TypeError("key must be an integer or a slice")
    

String.__len__ = __string_length
String.__contains__ = __string_contains
String.__getitem__ = __string_getitem


class Test(unittest.TestCase):

    def testStringLen(self):
        """testear que len(String("string of size 17") funciona y devuelve 17"""
        s = String("string of size 17")
        assert len(s) == 17
    
    def testStringIn(self):
        """testear que la sintaxis "A" in String("ABC") funciona"""
        s = String("ABC")
        assert "A" in s
        assert "N" not in s
    
    def testStringSubscriptable(self):
        """Testear que la sintaxis con indices String("ABCDEFG")[3] es valida"""
        s = String("ABCDEFG")
        assert s[0] == "A"
        assert s[1] == "B"
        assert s[6] == "G"
        assert s[-1] == "G"
        
    def testStringIndexOutOfBounds(self):
        """Testear que usar un indice mayor que la longitud de la cadena levanta un IndexError"""
        s = String("ABC")
        try:
            s[5]
            self.fail("IndexError should've been raised")

        except IndexError:
            pass
        
    def testStringIndexTypeError(self):
        """Testear que pasar algo que no sea entero o slice como indice levanta una TypeError"""
        s = String("ABC")
        try:
            s['asda']
            self.fail("TypeError should've been raised")
        except TypeError:
            pass
        
    def testStringSlice(self):
        """testear que se pueden usar slices como String("ABCDEF")[2:4]"""
        s = String("ABCDEFG")
        assert s[2:4] == "CD"
        
    def testStringReverse(self):
        """testear que se puede usar reversed(s) para revertir el orden de los caracteres"""
        s = String("ABCDEFG")
        self.assertEquals(''.join(reversed(s)), "GFEDCBA")
        

if __name__ == "__main__":
    unittest.main()