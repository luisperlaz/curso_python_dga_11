import java.io.IOException;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;


public class JythonScripting {
	
	public static void main(String[]args) throws IOException, ScriptException {
		
        ScriptEngineManager mgr = new ScriptEngineManager(); 
        ScriptEngine eng = mgr.getEngineByName("python");
        System.out.println("eng: " + String.valueOf(eng));
        
        eng.put("var1", new Integer(257));
        
        eng.eval("print 'var1 from python: %s' % var1");
        Integer var1 = (Integer) eng.eval("var1");
        System.out.println("var1 returned to java: " + var1);
        
        eng.eval("import sys");
        eng.eval("print sys.version");
    }
}
