package lab6;

public class Item {

	public ProductType type;
	public int quantity=1;
	public String comment = "" ;

	public Item (ProductType product , int quantity , String comment)
	{
		type = product;
		if (quantity<=0)
		{
			//return NOT POSSIBLE
		}
		else
			{
			this.quantity = quantity;
			}
		this.comment=comment;
	}

	public Item(ProductType product , int quantity )
	{
		if (quantity <= 0)
		{
			
		}
		else
		{
			this.quantity = quantity;
		}
		type = product;
	}
		
	public Item (ProductType product)
	{
		type = product;
	}

	public void AddItems(int quantity)
	{
		this.quantity += quantity;
	}

	public boolean remove(int number)
	{
		if (quantity > number)
		{
			return true;
		}
		else
		{
			return false;
		}
	}

	public int getQuantity()
	{
		return quantity;
	}

	public double getTotalPrice()
	{
		double TotalPrice = quantity*type.getPrice();
		return TotalPrice;
	}

	public double getTotalWeight()
	{
		double TotalWeight = quantity*type.getWeight();
		return TotalWeight;
	}

	public String toString()
	{
		String item = type + " " + Integer.toString(quantity) + " " + comment;
		return item;
	}

	public boolean equals(Item other)
	{
		if(type==other.type)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
}