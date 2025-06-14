
import java.util.Scanner;
public class MediaPonderada {
    public static void main(String[] args) {

        int cod1, num1, cod2, num2;
        double valor1, valor2, resultado;

        Scanner valor = new Scanner (System.in);

        System.out.println("Informe o código da primeira peça");
        cod1 = valor.nextInt();

        System.out.println("Informe o número de peças");
        num1 = valor.nextInt();

        System.out.println("Informe o valor de cada peça");
        valor1 = valor.nextDouble();

        System.out.println("Informe o código da segunda peça");
        cod2 = valor.nextInt();

        System.out.println("Informe o número de peças");
        num2 = valor.nextInt();

        System.out.println("Informe o valor de cada peça");
        valor2 = valor.nextDouble();

        resultado = valor1 * num1 + valor2 * num2;

        System.out.printf("Pagamento = R$ %.2f" , resultado);

        valor.close();

    }
