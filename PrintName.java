
public class PrintName implements IArithmeticsDiv, IArithmeticsDiff, IArithmeticMult, IArithmeticsAdd {
//Stop tripping', I'm tripping' off the powerstatek
    public static void main(String[] args) {

        System.out.println("Myszojelenie Operations snapeeek");
        System.out.println("Developer AdamWojtczak");
        System.out.println("Tester AndrzejBilant");
        System.out.println("Operations Snapeeek");
        System.out.println("Developer BartoszKowalczyk98");
    }
    //No one man should have all that power

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
    //The clock's ticking', I just count the hours

    @Override
    public double Difference(double A, double B) {
        return A - B;
    }
}

