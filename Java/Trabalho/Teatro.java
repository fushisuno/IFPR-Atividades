package Trabalho;

import java.util.Scanner;

public class Teatro {
    static Scanner ler = new Scanner(System.in);
    static int mat[][] = new int[15][15];
    static double ingresso = 50;
    static int qtdEstudantes = 0;
    static int polConfirm = 0;
    static int polReser = 0;
    static  double valorTot = 0;

    public static void main(String[] args) {
        for (int j = 0; j < mat.length; j++) {
            for (int i = 0; i < mat.length; i++) {
                mat[i][j] = -1;
            }
        }

        while (true) {
            System.out.println("              Menu              ");
            System.out.println("0 - Área Administrativa \t1 - Área de Cliente");
            System.out.println("Escolha sua operação: ");
            int op = ler.nextInt();
            System.out.println();
            if(op == 1 || op ==0){
                if(op == 0){
                    adm();
                }else{
                    client();
                }
            }else
            break;
            
        }
    }

    public static void mapAssentos(int mat[][]) {
        System.out.println(
                "################################\n" +
                        "             Palco              \n" +
                        "################################\n");

        System.out.println("   0 0 0 0 0 0 0 0 0 0 1 1 1 1 1");
        System.out.println("   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4");
        for (int i = 0; i < mat.length; i++) {
            System.out.print((i < 10 ? "0" + i : i) + " ");
            for (int j = 0; j < mat.length; j++) {
                System.out.print((mat[i][j] == -1? "_" : mat[i][j] == 0? "R" : "X") + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void adm() { 
        System.out.println("Olá, seja bem vindo");
        while(true){
             menuAcess(0);
            System.out.println("Escolha sua operação: ");
            int op = ler.nextInt();
            if(op == 4)
            break;

            switch (op) {
                case 1:
                    System.out.println();
                    mapAssentos(mat);
                    break;
                case 2:
                System.out.println("Informe o novo valor do ingresso: ");
                ingresso = ler.nextDouble();
                break;

                case 3:
                int polVaz = (15*15) - (polConfirm + polReser);
                System.out.println("           Relatórios           ");
                System.out.println("- Quantidade de Poltronas:");
                System.out.printf("   Confirmadas: %d\n", polConfirm);
                System.out.printf("   Reservadas: %d\n", polReser);
                System.out.printf("   Vazias: %d\n", polVaz);
                System.out.println("- Total de Estudantes: " + qtdEstudantes);
                System.out.printf("- Total arrecadado: R$ %.2f\n", valorTot);
                break;
            }
            System.out.println();
        }
    }

    public static void client() {
        System.out.println("Olá, seja bem vindo");
        while(true){
             menuAcess(1);
            System.out.println("Escolha sua operação: ");
            int op = ler.nextInt();
            if(op == 5)
            break;

            System.out.println();
            switch (op) {
                case 1:
                    System.out.println();
                    mapAssentos(mat);
                    break;
                case 2:
                    System.out.println("É estudante ? (S/N)");
                    int estud = ler.next().toUpperCase().equals("S")? 1: 0;
                    System.out.println("Informe a fila: ");
                    int line = ler.nextInt();
                    System.out.println("Informe a coluna: ");
                    int column = ler.nextInt();
                    
                    System.out.println("1 - Reservar\n2 - Comprar");
                    int ops  = ler.nextInt();
                    if((line > -1 && line <15) && (column > -1 && column <15) && (ops > 0 && ops < 3)){
                        if(mat[line][column] != 1){
                            if(ops == 2){
                                mat[line][column] = 1;
                                if(estud == 1){
                                    qtdEstudantes += 1;
                                    valorTot += ingresso/2;
                                }else{
                                    valorTot += ingresso;
                                }
                                polConfirm++;
                            }else{
                                mat[line][column] = 0;
                                polReser++;
                            }
                            
                        }else
                            System.out.println("Assento já está sendo ocupado");                           
                    }else{
                        System.out.println("Valores inválidos");
                    }

                    break;

                case 3:
                    System.out.println("Informe a fila: ");
                    line = ler.nextInt();
                    System.out.println("Informe a coluna: ");
                    column = ler.nextInt();
                    if((line > -1 && line <15) && (column > -1 && column <15)){
                            if(mat[line][column] == 0){
                            mat[line][column] = -1;
                            polReser--;
                        }else
                            System.out.println("Reserva inválida");  
                    }else{
                        System.out.println("Valores inválidos");
                    }
                    break;

                    case 4:
                        System.out.println("É estudante ? (S/N)");
                        estud = ler.next().toUpperCase().equals("S")? 1: 0;
                        System.out.println("Informe a fila: ");
                        line = ler.nextInt();
                        System.out.println("Informe a coluna: ");
                        column = ler.nextInt();
                        if((line > -1 && line <15) && (column > -1 && column <15)){
                            if(mat[line][column] == 0){
                                mat[line][column] = 1;
                                if(estud == 1){
                                    qtdEstudantes += 1;
                                    valorTot += ingresso/2;
                                }else{
                                    valorTot += ingresso;
                                }
                                polConfirm++;
                                polReser--;
                            }else
                                System.out.println("Reserva inválida");  
                        }else{
                            System.out.println("Valores inválidos");
                        }
                        break;
            }
            System.out.println();
        }
    }

    public static void menuAcess(int serv) {
        System.out.println("              Menu              ");
        System.out.println(serv == 1
                ? "1 - Visualizar Assentos\n2 - Realizar Reserva\n3- Cancelar Reserva\n4 - Confirmar Reserva\n5 - Sair da área de cliente"
                : "1 - Visualizar Assentos\n2 - Modificar Ingresso\n3 - Gerar Relatórios\n4 - Sair da área administrativa");
    }
}
