import java.util.Scanner;

public class MultiplicaTresNumeros {

    public static void main(String[] args) {

        String Mensagem = "Bem-vindo! Insira três números para realizar a operação.";

        int n1, n2, n3;
        int total;

        System.out.println(Mensagem);

        Scanner scanner = new Scanner (System.in);

        System.out.println("Digite o primeiro número: ");
        n1 = scanner.nextInt();

        System.out.println("Digite o segundo número: ");
        n2 = scanner.nextInt();

        System.out.println("Digite o terceiro número: ");
        n3 = scanner.nextInt();

        System.out.println("Resultado da operação: " + (n1 * n2) * n3);
        total = scanner.nextInt();

        scanner.close();


    }

}
