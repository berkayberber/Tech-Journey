package Lab5;

public class SimpleList {
	protected SimpleList next;
	protected int value;
	public SimpleList(int val) {
		value=val;
		next=null;
	}
	public static SimpleList addElem(SimpleList start, int val) {
		SimpleList elem= new SimpleList(val);
		elem.next=start;
		return elem;
	}
	public static String toString(SimpleList start) {
		if (start==null)
			return "[end]";
		return "["+start.value+"]\t"+toString(start.next);
	}
	public static void TotalSumR(SimpleList start, int sum) {
		if (start==null) {
			System.out.println(sum);
			return;
		}if (start.value>0) {
			sum=sum+start.value;
		}
		TotalSumR(start.next, sum);
		
	}
	public static int getSize(SimpleList start) {
		if (start==null) {
			return 0;
		}
		return (getSize(start.next)+1);
	}
	public static int TotalSumI(SimpleList start) {
		int sum=0;
		if (start==null) {
			return sum;
		} 
		int y=getSize(start);
		for (int x=0; x<y; x++) {
			if (start.value>0)
			sum=sum+start.value;
			start=start.next;
		}
		return sum;
	}
	public static void main(String[] args) {
		int [] arr= {23,-1,34,2,1,43,1,-13,32};
		String s="";
		SimpleList test=new SimpleList(arr[arr.length-1]);

		for (int x=arr.length-2; x>=0; x--) {
			test=addElem(test,arr[x]);
		}
		s=toString(test);
		int sum=0;
		System.out.println("The list with element that are taken from an integer array is: "+'\n'+s);
		System.out.println("The total sum of the positive elements in the list using iterative method: "+TotalSumI(test));
		System.out.print("The total sum of the positive elements in the list using recursive method: ");
		TotalSumR(test,sum);
	}
}

