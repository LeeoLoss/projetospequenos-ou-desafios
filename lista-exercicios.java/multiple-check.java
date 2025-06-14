import java.util.Scanner;
public class MediaPonderada {
    public static void main(String[] args) {

        int num1, num2;

        Scanner sc = new Scanner(System.in);

        System.out.println("Informe dois números.");
        num1 = sc.nextInt();
        num2 = sc.nextInt();

        if (num1 % num2 == 0 || num2 % num1 == 0) {
            System.out.println("São múltiplos.");
        }
        else {
            System.out.println("Não são múltiplos.");
        }

        sc.close();

    }
}
