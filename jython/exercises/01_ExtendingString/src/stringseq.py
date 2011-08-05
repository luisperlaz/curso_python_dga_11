'''
Created on Jul 27, 2011

@author: Luis Perez

Ejercicio creado con el proposito de mostrar la capacidad de extender una clase Java
(En este caso, java.lang.String), para que adquiera caracteristicas de python.

Modificaremos la clase String para que adquiera capacidades como subscripting (ej: String("ABC")[3])
ver los tests vacios o por completar mas abajo.

Ayuda:
    Necesario implementar en java.lang.String los metodos __len__, __contains__, y __getitem__
    Ver (http://docs.python.org/reference/datamodel.html)
'''
import unittest

from java.lang import String #@UnresolvedImport

#String.__len__ = __string_length
#String.__contains__ = __string_contains
#String.__getitem__ = __string_getitem


class Test(unittest.TestCase):
    
    def testStringLen(self):
        """testear que len(String("string of size 17") funciona y devuelve 17"""
        s = String("string of size 17")
        assert len(s) == 17
    
    def testStringIn(self):
        """testear que la sintaxis "A" in String("ABC") funciona"""
        self._implement_me()
    
    def testStringSubscriptable(self):
        """Testear que la sintaxis con indices String("ABCDEFG")[3] es valida"""
        self._implement_me()
        
    def testStringIndexOutOfBounds(self):
        """Testear que usar un indice mayor que la longitud de la cadena levanta un IndexError"""
        self._implement_me()
        
    def testStringIndexTypeError(self):
        """Testear que pasar algo que no sea entero o slice como indice levanta una TypeError"""
        self._implement_me()
        
    def testStringSlice(self):
        """testear que se pueden usar slices como String("ABCDEF")[2:4]"""
        self._implement_me()
        
    def testStringReverse(self):
        """testear que se puede usar reversed(s) para revertir el orden de los caracteres"""
        self._implement_me()
        
    def _implement_me(self):
        self.fail("Not yet implemented!")
        
if __name__ == "__main__":
    unittest.main()