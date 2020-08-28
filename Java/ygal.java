import java.util.Scanner;
public class atividade {
    public static void main(String[] args){
    
    Scanner input = new Scanner(System.in);
    String nome,idade,ano;
    System.out.println("Digite uma palavra: ");
       nome = input.nextLine();
    System.out.println("Digite sua idade: ");
       idade = input.nextLine();
    System.out.println("Digite o nascimento: ");
       ano = input.nextLine();



       System.out.println(nome);
       System.out.println(idade);
       System.out.println(ano);
    
}

}