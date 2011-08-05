package es.neodoo.pythoncourse.dictaccess;

import java.util.*;

public class CustomDict {
	
    public Map data;

    @SuppressWarnings("rawtypes")
	public CustomDict() {
        data = new HashMap();
    }
    
    public void __setitem__(Object key, Object value) {
        data.put(key, value);
    	System.out.println(String.format("Added key %s with value %s", key, value));
    }
    
    public Object __getitem__(Object key) {
    	if (data.containsKey(key)) {
            Object value = data.get(key);
        	System.out.println(String.format("Found key %s  with value %s", key, value));
            return value;
                
        } else {
        	System.out.println(String.format("Key %s not found", key));
        	return null;
        }
    }
    
    public boolean __contains__(Object key) {
    	
        if (data.containsKey(key)) {
        	System.out.println(String.format("Found key %s", key));
            return true;
        } else {
        	System.out.println(String.format("Key %s not found", key));
            return false;
        }
    }
}