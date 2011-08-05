'''
@author: Luis Perez

Ejemplo basico de obtencion y modificacion de propiedades en objetos java 
que siguen la convencion JavaBeans.
'''

if __name__ == '__main__':
    
    from es.neodoo.jythoncourse.jproperties import HighSchool
    hschool = HighSchool("instituto1", "Zaragoza", numberOfStudents=100)
    
    print("%s in %s for %i students" % (hschool.name, hschool.city,
                                        hschool.numberOfStudents))
    hschool.numberOfStudents = 200
    print(hschool.numberOfStudents)
    
    