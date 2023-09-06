import java.io.PrintWriter;
import java.util.Scanner;
public class arq2 {
    
    static Scanner ler = new Scanner(System.in);

    public static void main(String[] args){

        try{
            for (int i = 1; i < 11; i++) {
                PrintWriter saida = new PrintWriter("./Java/Arquivos/Arqs/arq" + i + ".txt");
                for (int j = 1; j <= i; j++) {
                     saida.printf("%d\n", j);
                }
                saida.close();
            }
        }catch(Exception e){
            System.out.println("");
        }

    }
}
