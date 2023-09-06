import java.io.FileWriter;
import java.util.Scanner;
public class files {
    
    static Scanner ler = new Scanner(System.in);

    public static void main(String[] args){
        FileWriter arq;
        try{
            arq = new FileWriter("./Java/Arquivos/File/file.txt", true);
            arq.write(String.format("\nTetse 90", 100));
            arq.close();
        }catch(Exception e){
            System.out.println("");
        }

    }
}
