
public class PrintName implements IArithmeticsDiv, IArithmeticsDiff, IArithmeticMult, IArithmeticsAdd {

    public static void main(String[] args) {
        //ok
        System.out.println("Myszojelenie Operations snapeeek");
        System.out.println("Developer AdamWojtczak");
        //plz
        //now it's better
        System.out.println("Tester AndrzejBilant");
        System.out.println("Operations Snapeeek");
        //what am i even doing
        System.out.println("Developer BartoszKowalczyk98");
        //halp me
        //at least i think

        //now am git
        //haha
        //lame joke sry

    }


    @Override
    public double Addition(double A, double B) {
        return A + B;
    }

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
