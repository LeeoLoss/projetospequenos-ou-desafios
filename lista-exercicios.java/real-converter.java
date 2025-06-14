import java.util.Scanner;

public class ConversorReal {

    public static void main(String[] args) {

        Scanner ConversorReal = new Scanner (System.in);

        System.out.println("Conversor de dólar para real");

        System.out.println("Digite a cotação do dólar: U$");
        double dolar_cotacao = ConversorReal.nextDouble();

        System.out.println("Digite o valor em dólar: U$");
        double dolar_valor = ConversorReal.nextDouble();

        double real_valor = dolar_cotacao * dolar_valor;

        System.out.printf("O valor em reais é: R$ %.2f%n" , real_valor);

        ConversorReal.close();
    }


}
