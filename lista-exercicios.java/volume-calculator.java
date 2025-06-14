import java.util.Scanner;

public class MediaPonderada {

    public static void main(String[] args) {

        Scanner Volume = new Scanner (System.in);

        System.out.println("Informe o raio: ");
        double raio = Volume.nextDouble();

        System.out.println("Informe a altura: ");
        double altura = Volume.nextDouble();

        double volume = 3.14159 * raio * raio * altura;

        System.out.printf("Este é o volume: %.2f%n" , volume);


    }

}
