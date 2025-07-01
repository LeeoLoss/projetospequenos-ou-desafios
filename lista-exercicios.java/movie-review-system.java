import java.util.Scanner; // Importa a classe Scanner, usada para ler entradas do usuário

public class Condicional { // Definição da classe pública

    public static void main(String[] args) { // Ponto de entrada da aplicação

        Scanner scanner = new Scanner(System.in); // Cria o objeto scanner para ler entradas pelo teclado

     // Solicita ao usuário as informações do filme (nome, inclusão no plano, nota e ano de lançamento) e realiza a leitura dos dados
        System.out.print("Digite o nome do filme: ");
        String nomeFilme = scanner.nextLine();

        System.out.print("O filme está incluído no plano? (true/false): "); 
        boolean incluidoNoPlano = scanner.nextBoolean(); //

        if (!incluidoNoPlano) { // Verifica se o filme NÃO está incluído no plano
            System.out.println("Atenção: este filme não está incluído no seu plano. Pode haver custos adicionais.");
        }

        System.out.print("Digite a nota do filme: "); 
        double notaDoFilme = scanner.nextDouble();

        System.out.print("Digite o ano de lançamento: "); 
        int anoDeLancamento = scanner.nextInt();

        // Verifica se o filme é um lançamento recente e bem avaliado
        if (anoDeLancamento >= 2022 && notaDoFilme >= 8.0) {
            System.out.println("Lançamento que os clientes estão curtindo!"); // Mensagem para filmes recentes e populares
        } else {
            System.out.println("Filme antigo e/ou não popular que vale a pena assistir"); // Mensagem alternativa
        }

        scanner.close(); // Fechando o objeto
    }
}
