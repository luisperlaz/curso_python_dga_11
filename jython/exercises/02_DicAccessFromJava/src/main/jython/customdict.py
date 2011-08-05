'''
Created on Jul 27, 2011

@author: Luis Perez

Ejercicio creado con el proposito de mostrar la capacidad de emular parcialmente la funcionalidad
de un diccionario python, implementando los metodos necesarios desde Java, y haciendo uso
de ellos desde jython.

Ayuda:
    Aunque java.util.HashMap ya tiene la funcionalidad requerida, puesto que jython lo integra
    por defecto, nuestra clase hara uso de ella para simplificar la implementacion.
    
    Sera necesario implementar los metodos __contains__, __getitem__, y __setitem__.
    Ver (http://docs.python.org/reference/datamodel.html)
'''
import unittest

from es.neodoo.pythoncourse.dictaccess import CustomDict

class Test(unittest.TestCase):
    
    def test_populate_read_dict(self):
        d = CustomDict()
        
        d['key1'] = "value1";
        d[5] = "value2"
        
        self.assertEquals(d['key1'], "value1")
        self.assertEquals(d[5], "value2")
        
    def test_in_dict_syntax(self):
        """testear que la sintaxis "key" in customDict funciona"""
        d = CustomDict()
        
        d['key1'] = "value1";
        d[5] = "value2"
        
        self.assertTrue("key1" in d)
        self.assertFalse(3 in d)
    
    def test_inexistent_key_return_None(self):
        """Testear que pasar una clave que no existe devuelve None"""
        d = CustomDict()
        assert d['nonexistent'] == None
        
if __name__ == "__main__":
    unittest.main()