public enum ProductType {
    BREAD (3.5), MILK(2.2), TEA(15.0), BUTTER(7.5), OTHER(0.0);
    private double weight;
    public static ProductType fromString(String s) {
        s=s.toLowerCase().trim();  /* BreAd\t\t\n ->> bread\t\t\n ->>> bread    */
        switch(s) {
            case "bread": return BREAD;
            case "milk": return MILK;
            case "tea": return TEA;
            case "butter": return BUTTER;
            default: return OTHER;
        }
    }
    private ProductType(double weight) {
        this.weight=weight;
    }
    public double getWeihgt() {
        return weight;
    }
    public String show() {
        String s=this+ " ["+weight+"]";
        return s.toLowerCase();
    }
    public static void testMe() {
        ProductType p1=ProductType.BREAD;
        System.out.println(p1);
        p1=ProductType.fromString("tea");
        System.out.println(p1);
        printIt();
    }
    public static void printIt(){
        for (ProductType p: ProductType.values()) {
            System.out.println(p.show());
        }
    }
}