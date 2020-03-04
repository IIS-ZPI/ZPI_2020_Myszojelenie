public class PrintName implements IArithmeticsAdd{
    public static void main(String[] args) {

        System.out.println("Myszojelenie Operations snapeeek");
        System.out.println("Developer AdamWojtczak");
        System.out.println("Tester AndrzejBilant"); 
        System.out.println("Operations Snapeeek");
        System.out.println("Developer BartoszKowalczyk98");
    }

    @Override
    public double Addition(double A, double B) {
        return A+B;
    }
}
