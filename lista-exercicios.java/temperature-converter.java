import java .util.Scanner;


public class ConversorTemperatura {

    public static void main(String[] args) {

    double Celsius;

    Scanner conversao  = new Scanner (System.in);

    System.out.println("Digite a temperatura em Celsius: ");
    Celsius = conversao.nextDouble();

    double Fahrenheit = (Celsius * 9 / 5) + 32;

    System.out.printf("A temperatura em Fahrenheit é: %.2f%n " , Fahrenheit);


    }

}
