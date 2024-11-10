public class BinaryNumber {
	private char[] binary;
    private int integerValue;

    public BinaryNumber(int val){
        this.binary = new char[32];
        this.binary = Integer.toBinaryString(val).toCharArray();
        this.integerValue = val;
    }
    public BinaryNumber (BinaryNumber bn){
        this.binary = new char[32];
        this.binary = bn.binary;
        this.integerValue = bn.integerValue;
    }
    public int getInteger(){
        return this.integerValue;
    }
    public String toString(){
        String s = String.valueOf(this.binary);
        int len = s.length();
        String add = "";
        for (int i = 0; i < 32-len; i++) {
            add=add+"0";
        }
        return add+s;
    }
    
    public BinaryNumber calcAND(BinaryNumber other){
        return  new BinaryNumber(other.getInteger() & this.getInteger());
    }
    public BinaryNumber calcAND(int val){
        return  new BinaryNumber(val & this.getInteger());
    }
    public static BinaryNumber calcAND(int val1, int val2){
        return  new BinaryNumber(val1 & val2);
    }
    public BinaryNumber calcOR(BinaryNumber other){
        return  new BinaryNumber(other.getInteger() | this.getInteger());
    }
    public BinaryNumber calcOR(int val){
        return  new BinaryNumber(val | this.getInteger());
    }
    public BinaryNumber calcXOR(BinaryNumber other){
        return  new BinaryNumber(other.getInteger() ^ this.getInteger());
    }
    public BinaryNumber calcXOR(int val){
        return  new BinaryNumber(val ^ this.getInteger());
    }
    
}
