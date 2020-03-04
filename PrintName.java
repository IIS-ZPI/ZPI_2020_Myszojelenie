public class PrintName implements IArithmeticsDiv{
    public static void main(String[] args) {

        System.out.println("Myszojelenie Operations snapeeek");
        System.out.println("Developer AdamWojtczak");
        System.out.println("Tester AndrzejBilant"); 
        System.out.println("Operations Snapeeek");
        System.out.println("Developer BartoszKowalczyk98");
    }

    @Override
    public double Division(double A, double B) {
        if(A==0||B==0){
            throw new ArithmeticException();
        }
        return A/B;
    }
}
