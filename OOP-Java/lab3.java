package xLabA3;


public class Lab3 {




	public static void prinArray(int[] anArray,int no) {      

			if (anArray!=null) {
	          if (anArray.length !=0) {
	        	   for (int i = 0; i <no; i++) {
	        		      System.out.print(anArray[i] + " ");
	   
	        		      
	               }	System.out.println();
	               for(int j=no; j<anArray.length;j++) {
	            	   System.out.print(anArray[j] + " ");
	               }
	               
	               
	            } else {
	            	System.out.println();
	                System.out.println("No data to print ");
	            }
	        }
	        else{
	            System.out.println("No data to print ");
	        }
		
		
		
    }
      public static boolean isAssending ( int[] arr){		
         return true;
      }															


      public static int[] createArray(int size){	 


		   int[] newArray = new int[size];
		   for(int i=0;i<size;i++) {
			   newArray[i]=11+2*i;
			  
		   }
		   return newArray;
		   

		   
		  		   
}

   
   
   
    public static double findAvarage(int [] arr) {				
    		
            int currElem = 0;
            int sum = 0;
            int counter = 0;
            double result;
            if(arr.length!=0)
            	{
            
                for (int i =0; i < arr.length; i++) {
                    currElem = arr[i];   	
                    sum = currElem + sum;
                    counter = counter + 1;

                }
                    	 
            }
            else  {
            	        	 // System.out.println("empty avarage: " +0);

            }
            
            result = (double) sum / counter;
         
            
            	

            
            return result;														


    }																




  public static int[] selectGreaterThan(int [] inArr,int limit) {		
        int currElem;
        int[]newArr = new int[6];
        
   
        for(int i=0;i<inArr.length;i++){
         
        currElem=inArr[i];
        
        if(currElem>limit){
    
            newArr[i]=currElem;
       
        }
   
        
    }
        
        return newArr;
  
    }


    public static void main(String[] args){						
   
    int[] testArray={7,12,15,0,5,8,};
    int[] emptyArray= {};
    int[] anotherArray;
    
    prinArray(testArray,3);
  
    prinArray(emptyArray,3);

    prinArray(null,3);
 
    anotherArray=createArray(8);				

    prinArray(anotherArray,8);							

        System.out.println("test avarage:" +findAvarage(testArray));

       System.out.println("empty avarage: "+findAvarage(emptyArray));

        anotherArray=selectGreaterThan(testArray,7);
        System.out.print(">7: ");
        prinArray(anotherArray,6);

        anotherArray=selectGreaterThan(testArray,77);
        System.out.print(">77: ");
        prinArray(anotherArray,6);
  
    }
}
