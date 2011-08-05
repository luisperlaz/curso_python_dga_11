package es.neodoo.jythoncourse.embedded;

import java.io.IOException;

import org.python.core.PyException;
import org.python.core.PyInteger;
import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.util.PythonInterpreter;


public class EmbeddedInterpreter {

	public static void main(String[]args) throws PyException, IOException
    {
        PythonInterpreter interp = new PythonInterpreter();
        interp.exec("import sys");
        interp.exec("print sys");
        
        interp.set("intvar", new PyInteger(10));
        interp.exec("print type(intvar)");
        interp.exec("x = intvar + 2");
        PyObject x = interp.get("x");
        
        int javaint = x.asInt();
        Integer javainteger = (Integer) x.__tojava__(Integer.class);
        System.out.println("x: " + javaint);
        
        PyObject localvars = interp.getLocals();
        
        localvars.__setitem__("var1", new PyString("hello!"));
        interp.set("localvars", localvars);
        interp.exec("print(var1)");
    }
}
