'''
@author: Luis Perez

Ejemplo basico de codigo jython que hace uso de una clase Java
'''

from java.security import MessageDigest

def calc_md5(text):
    md5 = MessageDigest.getInstance("md5")
    md5.update(text)
    return jarray_to_hex_s(md5.digest())   #Aqui reside la unica complejidad

def jarray_to_hex_s(jarray_):
    """Convertir un array de bytes java en una representacion hexadecimal del mismo"""
    return "".join(["%02X" % (x & 0xFF) for x in jarray_.tolist()])

if __name__ == "__main__":
    print("md5 of 'hello!!': %s'" % calc_md5("hello!!"))