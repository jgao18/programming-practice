# Languages like Java have fixed size arrays, but also resizeable ArrayLists; This class defines a resizeable array
# In contrast, languages like Python only have resizeable arrays

public class ResizableArray { 
	private int[] array = new int[10];
	private int size = 0;
}

public int size() {
	return size;
}

public void set(int index, int item) {
	if (index < 0 || index >= array.length) {
		throw new ArrayIndexOutOfBoundsException(index);
	}
	array[index] = item;
}

public void append(int item) {
	if (size == array.length) {
		private int[] newArray = new int[size*2];
		for (int i = 0; i < size; i++) {
			newArray[i] = array[i];
		}
		array = newArray;
	}
	array[size] = item;
	size++;
}

public int get(int idex) {
	if (index < 0 || index >= array.length) {
		throw new ArrayIndexOutOfBoundsException(index);
	}
	return array[index];
}