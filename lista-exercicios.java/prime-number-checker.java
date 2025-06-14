import java.util.Scanner;


public class VerificadorPrimo {

    public static void main(String[] args) {

        Scanner Primo = new Scanner(System.in);

        System.out.println("Informe um número: ");
        int num = Primo.nextInt();
        for(int i = 2; i <= num; i++) {
            boolean primo = true;
            for(int k = 2; k < i; k++) {
                if (i % k == 0) {
                    primo = false;
                }
            }
        if(primo)   {
            System.out.println(i);
            
        Primo.close();
        }
        }
    }
