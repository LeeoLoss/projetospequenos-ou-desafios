import java.util.Scanner;

public class VerificadorMaioridade {

	public static void main(String[] args) {
	
        Scanner idade = new Scanner(System.in);

        System.out.println("Informe a sua idade: ");
        int numero = idade.nextInt();

        if (numero >= 18) {
            System.out.println("Sua idade é " + numero + ", então é maior de idade.");
        }   else {
            System.out.println("Sua idade é " + numero + ", então é menor de idade.");
        }

        idade.close();

    }
