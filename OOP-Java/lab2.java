import java.util.Scanner;
public class GreatertThan10 {

	public static void main (String [] args)
	{
		int sum=0;
		int currElem;
		
		Scanner sc = new Scanner (System.in);
		
		while(sc.hasNextInt())
		{
			currElem=sc.nextInt();
			
			if(currElem>10)
			{
				sum=sum+currElem;
			}
			else
			{
				continue;
			}
			
		}
		
		sc.close();
		
		System.out.print("the sum is "+sum+"\n");
		System.exit(0);
	}
}
