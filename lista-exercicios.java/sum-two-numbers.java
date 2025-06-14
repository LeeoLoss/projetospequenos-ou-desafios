import java.util.Scanner;


public class SomaDoisNumeros {

    public static void main(String[] args) {

        Scanner Soma = new Scanner(System.in);

        int a, b, soma;


        System.out.println("Digite o primeiro número para realizar a soma: ");
        a = Soma.nextInt();

        System.out.println("Digite o segundo número para realizar a soma: ");
        b = Soma.nextInt();

        soma = a + b;

        System.out.print("O resultado de sua soma é: " + soma);

        Soma.close();
    }

}
