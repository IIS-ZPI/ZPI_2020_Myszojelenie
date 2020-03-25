
public class PrintName implements IArithmeticsDiv, IArithmeticsDiff, IArithmeticMult, IArithmeticsAdd {
//Stop tripping', I'm tripping' off the powerstatek
    public static void main(String[] args) {
        //ok
        System.out.println("Myszojelenie Operations snapeeek");
        System.out.println("Developer AdamWojtczak");
        //plz
        //now it's better
        System.out.println("Tester AndrzejBilant");//Andrzej RachunekMrowka drugi komentarza adamwojtczak
        System.out.println("Operations Snapeeek");
        //what am i even doing
        System.out.println("Developer BartoszKowalczyk98");//komentarz uno AdamWojtczak
        //halp me
        //at least i think

        //now am git
        //haha
        //lame joke sry

    }

    //No one man should have all that power

    /*
    * Był ostatnio zaobserwowany w Wietnamie
    Choć naukowcy myśleli, że już dawno wyginął
    Znany również jako Kanczyl srebrnogrzbiety*/


    @Override
    public double Addition(double A, double B) {//Parostatkiem w piękny rejs, statkiem na parę w piękny rejs
        return A + B;
    } //konentarz zadanie 6

    @Override
    public double Multiplication(double A, double B) {
        return A * B;
    }
    /* Ma ma ma ma ma małe nóżki
    A do tego duży tułów
    Ma kopytka i twarz jak gryzoń */
    @Override
    public double Division(double A, double B) {
        if (B == 0) {//I'm living' in that 21st century
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

