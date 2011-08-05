'''
Created on Aug 1, 2011

@author: luis
'''

from es.neodoo.jythoncourse.factory import HighSchoolType

class HighSchool(HighSchoolType):
    def __init__(self, name, city):
        self._name = name
        self._city = city
        
    def getName(self):
        return self._name
    
    def getCity(self):
        return self._city
    
    def setName(self, name):
        self._name = name

    def setCity(self, city):
        self._city = city