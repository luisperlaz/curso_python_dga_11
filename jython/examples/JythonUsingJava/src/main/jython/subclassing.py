'''
Created on Jul 31, 2011

@author: luis
'''

from es.neodoo.jythoncourse.jproperties import HighSchool

class ExtendedHighSchool(HighSchool):
    def __init__(self, name, city, address):
        HighSchool.__init__(self, name, city) #@UndefinedVariable
        self.address = address
    

if __name__ == '__main__':
    eh = ExtendedHighSchool("Centro 1", "Zaragoza", "Independencia, 2")
    print(eh.address)
