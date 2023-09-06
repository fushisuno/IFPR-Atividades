
import java.io.File;
import java.util.Scanner;

public class read_arq {
    public static void main(String[] args){
        File arq;
        Scanner ler;

        try{
            arq = new File("./Java/Arquivos/File/file.txt");
            ler = new Scanner(arq);

            while(ler.hasNext()){
                int j = ler.nextInt();
                System.out.println(j);
            }

            ler.close();
        }catch(Exception e){
            System.out.println("");
        }

 }
}
