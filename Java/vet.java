import java.util.Scanner;
public class vet {
    
    static Scanner ler = new Scanner(System.in);

    public static void main(String[] args){
        System.out.println((120 + "").length());
        int vet[] = new int[5];
        for (int i = 0; i < vet.length; i++) {
            vet[i] = ler.nextInt();
        }

        System.out.print("Seu vetor é: ");
        for (int i = 0; i < vet.length; i++) {
            System.out.print(vet[i] + " ");
        }
        System.out.println();

    }
}
