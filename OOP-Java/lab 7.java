package inheritance;

public class Bag {

	
	    int bagCapacity;
	    SimpleItemList itemsList;
	    boolean premiumQuality;
	    boolean extremelyRobust;

	    public Bag (boolean robustness, int bagCapacity){
	        this.extremelyRobust=robustness;
	        this.bagCapacity=bagCapacity;
	        this.itemsList = new SimpleItemList();
	    }
	    public Bag (boolean premiumQuality){
	        this.premiumQuality=premiumQuality;
	        this.bagCapacity=5;
	        this.itemsList = new SimpleItemList();
	    }
	    public Bag(int bagCapacity){
	        this.bagCapacity = bagCapacity;
	        this.itemsList = new SimpleItemList();
	    }
	    public void removeAllItems(){
	    	System.out.println("You removed all type of items");
	        this.itemsList.removeAllItems(this.itemsList);
	    }
	    public boolean putIn(Item item){ // dummy 
	        if (bagCapacity+1 >= item.quantity+this.itemsList.getItemCount(itemsList)){
	            System.out.println("Added " + item.toString());
	            this.itemsList.addItem(this.itemsList,item);
	            return true;
	        }
	        else {
	        	System.out.println("You tried to add more than capacity");
	        	return false;
	        }
	        
	    }
	    public boolean remove(ProductType pr){
	    
	    
	        return this.itemsList.remove(pr,this.itemsList);
	    

	    }
	    public boolean remove(ProductType product, int n){ 
	        System.out.println("Removing "+ n+ " "+ product+" from the "+getClass());
	        return this.itemsList.remove(product,this.itemsList,n);
	    }


	    public boolean equals(Object other){
	    	if (this == other) {
	            return true;
	        } else if (other == null) {
	            return false;
	        } else if (other instanceof Bag) {
	            Bag bg = (Bag) other;
	            if (bg.getTotalWeight().equals(this.getTotalWeight()) &&
	                    this.bagCapacity == ((Bag) other).bagCapacity &&
	                    this.itemsList.getItemCount(this.itemsList)== bg.itemsList.getItemCount(bg.itemsList) ){
	                return true;
	            }
	        }
	        return false;
	    }
	    public String getTotalWeight(){
	        double total = 0;
	        if (this.itemsList==null){
	            return "0";
	        }
	        SimpleItemList tmp = this.itemsList.next;
	        while (tmp!=null){
	            total += tmp.item.quantity * tmp.item.type.getWeihgt();
	            tmp=tmp.next;
	        }
	        return String.format("%.1f",total);
	    }
	    public String toString() {
	        return "This is a "+this.getClass()+", containing  bag capacity "+(this.bagCapacity-this.itemsList.getItemCount(this.itemsList)+1) + " and "
	                +this.getTotalWeight()
	                + " lbs of items.";
	    }
}