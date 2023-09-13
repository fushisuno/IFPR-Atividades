import java.io.File;
import java.util.Scanner;

public class texto {
    public static void main(String[] args){
        File arq;
        Scanner ler;

        try{
            arq = new File("./Java/Arquivos/File/texto.txt");
            
            for (int cod = 97; cod  < 123; cod++) {
                char pos = (char) cod;
                int add = 0;
                ler = new Scanner(arq);

                while(ler.hasNext()){
                    String j[] = ler.next().split("");
                    for(int i = 0;i<j.length;i++){
                        if(pos == j[i].toLowerCase().charAt(0)){
                            add++;
                        }
                    }
                }
                System.out.printf("Exitem %s letra(s) '%c'\n", add, pos);
                ler.close();
            }
        }catch(Exception e){
            System.out.println("");
        }
    }


    // a= 97  -> z=122
}
