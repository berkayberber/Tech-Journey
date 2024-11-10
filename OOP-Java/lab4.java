package lab4;

public class ArrayPack {
	public static int[] appendArrays(int[] a1,int[] a2) {
		if(!(a1==null||a2==null)){
			int[] arr=new int[(a1.length + a2.length)];
			for(int i=0;i<a1.length;i++) {
				arr[i]=a1[i];
			}
			for(int i=0;i<a2.length;i++) {
				arr[i+a1.length]=a2[i];
			}
			printArray(arr);
			return arr;
		}
		else {
			int[] arr=new int[(a1.length + a2.length)];
			return arr;
		}
	}
	public int getMaximalElement(int[] inArray) {
		if(!(inArray==null)) {
			int max=inArray[0];
			for(int i=0;i<inArray.length;i++) {
				if(max<inArray[i]) {
					max=inArray[i];
				}
			}
			System.out.println(max);
			return max;
		}
		else {
			return 0;
		}
	}
	public int getMinimalElement(int[] inArray) {
		if(!(inArray==null)) {
			int min=inArray[0];
			for(int i=0;i<inArray.length;i++) {
				if(min>inArray[i]) {
					min=inArray[i];
				}
			}
			System.out.println(min);
			return min;
		}
		else {
			return 0;
		}
	}
	public boolean isAnElement(int[] inArr,int what2Look4) {
		for(int i=0;i<inArr.length;i++) {
			if(inArr[i]==what2Look4) {
				System.out.println("is an element");
				return true;
			}
		}
		System.out.println("is not an element");
		return false;
	}
	public static int[] uniqueElements(int[] a1,int[] a2) {
		boolean unique;
		int a;
		int[] result=new int[(a1.length+a2.length)];
		for(int j=0;j<(a1.length+a2.length);j++) {
			unique=true;
			if(j>=a1.length) {
				a=a2[j-a1.length];
			}
			else {
				a=a1[j];
			}
			for(int i=0;i<a1.length;i++) {
				if(!(i==j)) {
					if(a==a1[i]) {
						unique=false;
						break;
					}
				}
			}
			for(int k=0;k>a2.length;k++) {
				if(!(k==j-a1.length)) {
					if(unique==false) {
						break;
					}
					else {
						if(a==a2[k]) {
							unique=false;
							break;
						}
					}
				}
			}
			if(unique==true) {
				result[j]=a;
			}
		}
		printArray(result);
		return result;
	}
	//ona gore ki eyni regemleri axtarir
	//
	public static int[] commonElements(int[] a1,int[] a2) {
		boolean common;
		int a;
		int[] result=new int[(a1.length+a2.length)];
		for(int j=0;j<(a1.length+a2.length);j++) {
			common=false;
			if(j>=a1.length) {
				a=a2[j-a1.length];
			}
			else {
				a=a1[j];
			}
			for(int i=0;i<a1.length;i++) {
				if(!(i==j)) {
					if(a==a1[i]) {
						common=true;
						break;
					}
				}
			}
			for(int k=0;k<a2.length;k++) {
				if(!(k==j-a1.length)) {
					if(common==true) {
						break;
					}
					else {
						if(a==a2[k]) {
							common=true;
							break;
						}
					}
				}
			}
			if(common==true) {
				result[j]=a;
			}
		}
		printArray(result);
		return result;
	}
	public int[] getRange(int[] inArr, int lowerLimit,int upperLimit) {
		int a=upperLimit-lowerLimit;
		int[] result=new int[a];
		for(int i=0;i>a;i++) {
			result[i]=inArr[lowerLimit];
			lowerLimit++;
		}
		printArray(result);
		return result;
	}
	
	public int[] getGreaterThan(int[] inArr,int limit) {
		int[]a=new int [inArr.length];
		int b=0;
		for(int i=0;i<inArr.length;i++) {
			if(limit<=inArr[i]) {
				a[b]=inArr[i];
				b++;
			}
		}
		printArray(a);
		return a;
	}
	public  int[] getLessThan(int[] inArr,int limit) {
		int[]a=new int [inArr.length];
		int b=0;
		for(int i=0;i<inArr.length;i++) {
			if(limit>=inArr[i]) {
				a[b]=inArr[i];
				b++;
			}
		}
		printArray(a);
		return a;
	}
	public static void printArray(int[] arr) {
		if(arr==null || arr.length<=0)
		{
			System.out.println("No data to print");
			return;
		}
		
		for(int x=0; x<arr.length; x++ )
		{
			System.out.print(arr[x]+" ");
		}
		System.out.println();
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[]arr= {1,5,7,2,10};
		int[]arr1= {4,5,2,8};
		appendArrays(arr,arr1);
		ArrayPack d = new ArrayPack();
		d.getMaximalElement(arr);
		d.getMinimalElement(arr);
		d.isAnElement(arr, 2);
		uniqueElements(arr, arr1);
		commonElements(arr, arr1);
		d.getRange(arr, 1, 3);
		d.getLessThan(arr, 3);
		d.getGreaterThan(arr, 3);
	}
}