import java.io.File;
import java.util.Scanner;

public class texto2 {
    public static void main(String[] args){
        File arq;
        Scanner ler;
        int alf[] = new int[26];

        try{
            arq = new File("./Java/Arquivos/File/texto.txt");
            ler = new Scanner(arq);

            while(ler.hasNext()){
                String j= ler.next();
                for (int i = 0; i < j.length(); i++) {
                    for (int cod = 97; cod < 123; cod++) {
                        if(j.toLowerCase().charAt(i) == (char) cod){
                            alf[cod-97]++;
                        }
                    }
                }
            }
            ler.close();
            for (int cod = 97; cod < 123; cod++) {
                System.out.printf("Existem %d letra(s) '%c'\n", alf[cod-97], (char) cod);
            }
            
        }catch(Exception e){
            System.out.println("");
        }
    }


    // a= 97  -> z=122
}
