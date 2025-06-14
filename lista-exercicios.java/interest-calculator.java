import java.util.Scanner;

public class CalculadoraJuros {

    public static void main(String[] args) {


        Scanner Calculo = new Scanner (System.in);

        System.out.println("Digite um valor: ");
        double vp = Calculo.nextDouble();

        System.out.println("Digite o valor da taxa do juros: ");
        double juros = Calculo.nextDouble();

        System.out.println("Digite  a quantidade de anos: ");
        double anos = Calculo.nextDouble();

        double vf = vp*(1 + juros * anos);

        System.out.printf("O valor final é: R$ %.2f%n" , vf);

    }


}
