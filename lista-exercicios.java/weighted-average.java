import java.util.Scanner;

public class MediaPonderada {

    public static void main(String[] args) {

        String Mensagem = "Bem-vindo. Para consultar a média, insira suas notas.";

        float nota1, nota2, nota3;
        float peso1, peso2, peso3;
        float total;

        System.out.println(Mensagem);

        Scanner scanner = new Scanner (System.in);

        System.out.println("Digite sua primeira nota: ");
        nota1 = scanner.nextFloat();

        System.out.println("Digite o peso da primeira nota: ");
        peso1 = scanner.nextFloat();

        System.out.println("Digite sua segunda nota: ");
        nota2 = scanner.nextFloat();

        System.out.println("Digite o peso da segunda nota: ");
        peso2 = scanner.nextFloat();

        System.out.println("Digite sua terceira nota: ");
        nota3 = scanner.nextFloat();

        System.out.println("Digite o peso da terceira nota: ");
        peso3 = scanner.nextFloat();



        System.out.println("Sua média ponderada é: "+ (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3));
        total = scanner.nextInt();

        scanner.close();

        System.out.print("Não esqueça de fechar a janela ao finalizar.");

    }

}
