package es.neodoo.jythoncourse.jproperties;

public class HighSchool {

    private String name;
    private String city;
    private int numberOfStudents;

	public HighSchool(String name, String city){
        this.name = name;
        this.city = city;
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
}
