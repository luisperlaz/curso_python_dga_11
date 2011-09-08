'''
@author: Luis Perez

Ejemplo de uso de listas, sets, y maps de Java
'''

if __name__ == '__main__':
    
    from es.neodoo.jythoncourse.jproperties import HighSchool
    hschool = HighSchool("instituto1", "Zaragoza")
    
    languages = hschool.languages
    subjects = hschool.subjects
    props = hschool.properties
    
    print("* Languages:")
    for lang in languages: # El set de Java se comporta como python!
        print(lang)
        
    print("* subjects:")
    for subj in subjects: # La lista de Java se comporta como python!
        print(subj)
        
    if props["public"]:
        print("Public highschool")
        
    #props.items() # no!
        
    propsd = dict(props) #creamos un dict de python a partir del map de Java
    for key, value in propsd.items(): 
        print("%s: %s" % (key, value))
    
    props["public"] = False
    hschool.properties = props # en Java el dict de python implementa java.util.Map !
    
    