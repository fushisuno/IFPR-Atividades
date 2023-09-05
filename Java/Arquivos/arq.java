import java.io.PrintWriter;
import java.util.Scanner;
public class arq {
    
    static Scanner ler = new Scanner(System.in);

    public static void main(String[] args){
        String message = "Testa com arquivos java";

        try{
            PrintWriter saida = new PrintWriter("./Java/Arquivos/Txt/numeros.txt");
            PrintWriter pares = new PrintWriter("./Java/Arquivos/Txt/pares.txt");
            PrintWriter impares = new PrintWriter("./Java/Arquivos/Txt/impares.txt");
            for (int i = 0; i < 11; i++) {
                saida.printf("%d\n", i);
                if(i%2 == 0){
                    pares.printf("%d\n", i);
                }else{
                    impares.printf("%d\n", i);
                }
            }
            saida.close();
            pares.close();
            impares.close();
        }catch(Exception e){
            System.out.println("");
        }

    }
}
