import java.util.Scanner;

public class CalculoIMC {

    public static void main(String[] args) {

        Scanner IMC = new Scanner(System.in);

        System.out.println("Informe o seu peso: ");
        double peso =  IMC.nextDouble();

        System.out.println("Informe a sua altura: ");
        double altura =  IMC.nextDouble();

        double imc = peso / (altura * altura);

        System.out.printf("Segue o seu IMC: %.2f%n" , imc);

        IMC.close();

    }

}
