package es.neodoo.jythoncourse.factory;

import static org.junit.Assert.*;

import org.junit.Test;

public class HighSchoolFactoryTest {

	@Test
	public void test() {
		
		HighSchoolFactory factory = new HighSchoolFactory();
		HighSchoolType highSchool = factory.create("un centro", "una ciudad");
		
		assertEquals("un centro", highSchool.getName());
		assertEquals("una ciudad", highSchool.getCity());
		
		highSchool.setName("otro centro");
		highSchool.setCity("otra ciudad");
		
		assertEquals("otro centro", highSchool.getName());
		assertEquals("otra ciudad", highSchool.getCity());
	}

}
