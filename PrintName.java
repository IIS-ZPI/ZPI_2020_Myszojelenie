
public class PrintName implements IArithmeticsDiv, IArithmeticsDiff, IArithmeticMult, IArithmeticsAdd {

    public static void main(String[] args) {

        System.out.println("Myszojelenie Operations snapeeek");
        System.out.println("Developer AdamWojtczak");
        System.out.println("Tester AndrzejBilant");//Andrzej RachunekMrowka drugi komentarza adamwojtczak
        System.out.println("Operations Snapeeek");
        System.out.println("Developer BartoszKowalczyk98");//komentarz uno AdamWojtczak
    }


    @Override
    public double Addition(double A, double B) {
        return A + B;
    } //konentarz zadanie 6

    @Override
    public double Multiplication(double A, double B) {
        return A * B;
    }

    @Override
    public double Division(double A, double B) {
        if (B == 0) {
            throw new ArithmeticException();
        }
        return A / B;
    }

    @Override
    public double Difference(double A, double B) {
        return A - B;
    }
}
