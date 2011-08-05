package es.neodoo.jythoncourse.embedded;

import org.python.util.InteractiveConsole;

public class EmbeddedConsole {
	protected InteractiveConsole interp;

	public EmbeddedConsole() {
		if (System.getProperty("python.home") == null) {
			System.setProperty("python.home", "");
		}
		InteractiveConsole.initialize(System.getProperties(), null,
				new String[0]);
		interp = new InteractiveConsole();
	}

	public static void main(String[] args) {
		EmbeddedConsole con = new EmbeddedConsole();
		con.startConsole();
	}

	public void startConsole() {
		interp.interact("Hello from console.", null);
	}
}
