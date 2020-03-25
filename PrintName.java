public class PrintName implements IArithmeticsDiv, IArithmeticsDiff{

    public static void main(String[] args) {

        System.out.println("Myszojelenie Operations snapeeek");
        System.out.println("Developer AdamWojtczak");
        System.out.println("Tester AndrzejBilant");
        System.out.println("Operations Snapeeek");
        System.out.println("Developer BartoszKowalczyk98");
    }

    @Override
    public double Division(double A, double B) {
        if(B==0){
            throw new ArithmeticException();
        }
        return A/B;
    }
        
      @Override
    public double Difference(double A, double B) {
        return A-B;
    }
}
