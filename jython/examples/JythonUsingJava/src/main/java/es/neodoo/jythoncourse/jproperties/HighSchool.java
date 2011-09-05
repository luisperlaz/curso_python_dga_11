package es.neodoo.jythoncourse.jproperties;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

public class HighSchool {

    private String name;
    private String city;
    private int numberOfStudents;
    private Set<String> languages;
    private List<String> subjects;
    private Map<String, ? super Object> properties;

	public HighSchool(String name, String city){
        this.name = name;
        this.city = city;
        languages = new HashSet<String>();
        subjects = new ArrayList<String>();
        properties = new HashMap<String, Object>();
        
        languages.add("spanish");
        languages.add("english");
        properties.put("founded", "1975");
        properties.put("public", true);
        subjects.add("Mathematics");
        subjects.add("Physics");
    }

	public String getName() {
    	System.out.println("Getting name!");
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCity() {
    	System.out.println("Getting city!");
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    
    public int getNumberOfStudents() {
    	System.out.println("Getting students!");
		return numberOfStudents;
	}

	public void setNumberOfStudents(int numberOfStudents) {
		System.out.println("Setting students!");
		this.numberOfStudents = numberOfStudents;
	}
	
	
	public void passMap(Map m) {
		System.out.println(m.getClass().getCanonicalName());
		System.out.println(m.keySet().iterator().next());
	}

	public Set<String> getLanguages() {
			return languages;
	}

	public void setLanguages(Set<String> languages) {
		this.languages = languages;
	}

	public List<String> getSubjects() {
		return subjects;
	}

	public void setSubjects(List<String> subjects) {
		this.subjects = subjects;
	}

	public Map<String, ? super Object> getProperties() {
		return properties;
	}

	public void setProperties(Map<String, Object> properties) {
		this.properties = properties;
		
		System.out.println("Updated properties:");
		for (Iterator<Entry<String, Object>> it = properties.entrySet().iterator(); it.hasNext();) {
			Entry<String, Object> entry = it.next();
			String key = entry.getKey();
			Object value = entry.getValue();
			System.out.println(String.format("%s: %s", key, value));
		}
	}
}
