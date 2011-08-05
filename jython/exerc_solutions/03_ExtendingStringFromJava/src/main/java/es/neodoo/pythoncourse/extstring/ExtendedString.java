package es.neodoo.pythoncourse.extstring;

import java.io.UnsupportedEncodingException;
import java.nio.charset.Charset;
import java.util.Locale;

import org.python.core.PySlice;
import org.python.core.Py;


public class ExtendedString {
	
	private String string;
	
	public int __len__() {
		return string.length();
	}
	
	public boolean __contains__(String item) {
		return string.contains(item);
	}
	
	public String __getitem__(Object key) {
		
		if (key instanceof PySlice) {
			return getItemSlice((PySlice) key);
			
		} else if (key instanceof Integer) {
			return getItemIndex((Integer) key);
			
		} else {
			throw Py.TypeError("key must be an integer or a slice");
		}
		
	}
	
	
	/** Metodos delegados */
	 
	public ExtendedString(String string) {
		this.string = string;
	}

	public char charAt(int arg0) {
		return string.charAt(arg0);
	}

	public int codePointAt(int arg0) {
		return string.codePointAt(arg0);
	}

	public int codePointBefore(int arg0) {
		return string.codePointBefore(arg0);
	}

	public int codePointCount(int arg0, int arg1) {
		return string.codePointCount(arg0, arg1);
	}

	public int compareTo(String arg0) {
		return string.compareTo(arg0);
	}

	public int compareToIgnoreCase(String arg0) {
		return string.compareToIgnoreCase(arg0);
	}

	public String concat(String arg0) {
		return string.concat(arg0);
	}

	public boolean contains(CharSequence arg0) {
		return string.contains(arg0);
	}

	public boolean contentEquals(CharSequence arg0) {
		return string.contentEquals(arg0);
	}

	public boolean contentEquals(StringBuffer arg0) {
		return string.contentEquals(arg0);
	}

	public boolean endsWith(String arg0) {
		return string.endsWith(arg0);
	}

	public boolean equals(Object arg0) {
		return string.equals(arg0);
	}

	public boolean equalsIgnoreCase(String arg0) {
		return string.equalsIgnoreCase(arg0);
	}

	public byte[] getBytes() {
		return string.getBytes();
	}

	public byte[] getBytes(Charset arg0) {
		return string.getBytes(arg0);
	}

	public void getBytes(int arg0, int arg1, byte[] arg2, int arg3) {
		string.getBytes(arg0, arg1, arg2, arg3);
	}

	public byte[] getBytes(String arg0) throws UnsupportedEncodingException {
		return string.getBytes(arg0);
	}

	public void getChars(int arg0, int arg1, char[] arg2, int arg3) {
		string.getChars(arg0, arg1, arg2, arg3);
	}

	public int hashCode() {
		return string.hashCode();
	}

	public int indexOf(int arg0, int arg1) {
		return string.indexOf(arg0, arg1);
	}

	public int indexOf(int arg0) {
		return string.indexOf(arg0);
	}

	public int indexOf(String arg0, int arg1) {
		return string.indexOf(arg0, arg1);
	}

	public int indexOf(String arg0) {
		return string.indexOf(arg0);
	}

	public String intern() {
		return string.intern();
	}

	public boolean isEmpty() {
		return string.isEmpty();
	}

	public int lastIndexOf(int arg0, int arg1) {
		return string.lastIndexOf(arg0, arg1);
	}

	public int lastIndexOf(int arg0) {
		return string.lastIndexOf(arg0);
	}

	public int lastIndexOf(String arg0, int arg1) {
		return string.lastIndexOf(arg0, arg1);
	}

	public int lastIndexOf(String arg0) {
		return string.lastIndexOf(arg0);
	}

	public int length() {
		return string.length();
	}

	public boolean matches(String arg0) {
		return string.matches(arg0);
	}

	public int offsetByCodePoints(int arg0, int arg1) {
		return string.offsetByCodePoints(arg0, arg1);
	}

	public boolean regionMatches(boolean arg0, int arg1, String arg2, int arg3,
			int arg4) {
		return string.regionMatches(arg0, arg1, arg2, arg3, arg4);
	}

	public boolean regionMatches(int arg0, String arg1, int arg2, int arg3) {
		return string.regionMatches(arg0, arg1, arg2, arg3);
	}

	public String replace(char arg0, char arg1) {
		return string.replace(arg0, arg1);
	}

	public String replace(CharSequence arg0, CharSequence arg1) {
		return string.replace(arg0, arg1);
	}

	public String replaceAll(String arg0, String arg1) {
		return string.replaceAll(arg0, arg1);
	}

	public String replaceFirst(String arg0, String arg1) {
		return string.replaceFirst(arg0, arg1);
	}

	public String[] split(String arg0, int arg1) {
		return string.split(arg0, arg1);
	}

	public String[] split(String arg0) {
		return string.split(arg0);
	}

	public boolean startsWith(String arg0, int arg1) {
		return string.startsWith(arg0, arg1);
	}

	public boolean startsWith(String arg0) {
		return string.startsWith(arg0);
	}

	public CharSequence subSequence(int arg0, int arg1) {
		return string.subSequence(arg0, arg1);
	}

	public String substring(int arg0, int arg1) {
		return string.substring(arg0, arg1);
	}

	public String substring(int arg0) {
		return string.substring(arg0);
	}

	public char[] toCharArray() {
		return string.toCharArray();
	}

	public String toLowerCase() {
		return string.toLowerCase();
	}

	public String toLowerCase(Locale arg0) {
		return string.toLowerCase(arg0);
	}

	public String toString() {
		return string.toString();
	}

	public String toUpperCase() {
		return string.toUpperCase();
	}

	public String toUpperCase(Locale arg0) {
		return string.toUpperCase(arg0);
	}

	public String trim() {
		return string.trim();
	}
	
	
	private String getItemSlice(PySlice key) {
		
		int[] range = key.indicesEx(string.length());
		int start = range[0];
		int stop = range[1];
		
		return string.substring(start, stop);
	}

	private String getItemIndex(int index) {
		
		if (index < 0) {
			index = string.length() + index;
		}
		
		try {
			return String.valueOf(string.charAt(index));
			
		} catch (StringIndexOutOfBoundsException aio) {
			throw Py.IndexError("Invalid key");
		}
	}
	
}
