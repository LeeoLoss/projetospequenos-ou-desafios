import java.util.Scanner;

public class CalculadoraRetangulo {

    public static void main(String[] args) {

        double base, altura, area;

        Scanner sc = new Scanner(System.in);

        System.out.println("Insira o número da base do retângulo: ");
        base = sc.nextFloat();

        System.out.println("Insira o número da altura do retângulo: ");
        altura = sc.nextFloat();

        System.out.println("Esta é a área de seu retângulo: " + (area = base * altura));

        sc.close();

    }

}
