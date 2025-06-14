import java .util.Scanner;

public class ConversaoTemperatura {

    public static void main(String[] args) {

        double Celsius, Kelvin, Reamur, Rankine, Fahrenheit;

        Scanner converter = new Scanner(System.in);


        System.out.println("Digite um valor em celsius: ");
        Celsius = converter.nextDouble();

        Kelvin = Celsius + 273.15;
        Reamur = Celsius * 0.8;
        Rankine = (Celsius * 1.8) + 32 + 459.67;
        Fahrenheit = Celsius * 1.8;


        System.out.printf("A temperatura em Kelvin é: %.2f%n " , Kelvin);
        System.out.printf("A temperatura em Reamur é: %.2f%n " , Reamur);
        System.out.printf("A temperatura em Rankine é: %.2f%n " , Rankine);
        System.out.printf("A temperatura em Fahrenheit é: %.2f%n " , Fahrenheit);


    converter.close();


    }

}
