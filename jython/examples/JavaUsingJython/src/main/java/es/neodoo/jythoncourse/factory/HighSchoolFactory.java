package es.neodoo.jythoncourse.factory;

import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.util.PythonInterpreter;

public class HighSchoolFactory {
	
    private PyObject jyHighSchoolClass;
    
	public HighSchoolFactory() {
        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.exec("from highschool import HighSchool");
        jyHighSchoolClass = interpreter.get("HighSchool");
    }

    public HighSchoolType create(String name, String city) {
        PyObject highschoolObj = jyHighSchoolClass.__call__(new PyString(name),
                                                        new PyString(city));
        return (HighSchoolType) highschoolObj.__tojava__(HighSchoolType.class);
    }
}
