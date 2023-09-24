package Trabalho;

import java.util.Scanner;

public class Minado {
    static Scanner ler = new Scanner(System.in);
    public static void main(String[] args) {
        // -5: Bomba
        // 0: Vazio
        // -1: Pisado
        // -2: Aberto
        int tabuleiroTam    = 0;
        int qtdBombas       = 0;
        int op = 0;
        do{
            System.out.println("          Campo Minado          ");
            System.out.println("1 - Easy  \t2 - Normal\t3 - Hard");
            System.out.println("Escolha sua operação: ");
            op = ler.nextInt();
            if(op == 1){
                tabuleiroTam = 5;
                qtdBombas = 3;
                playGame(tabuleiroTam, qtdBombas);
                System.out.println();
            } else if(op == 2){
                tabuleiroTam = 10;
                qtdBombas = 20;
                playGame(tabuleiroTam, qtdBombas);
                System.out.println();
            }else if(op == 3){
                tabuleiroTam = 15;
                qtdBombas = 30;
                playGame(tabuleiroTam, qtdBombas);
                System.out.println();
            }else
                break;
        }while(op > 0 && op < 4);
    }

    public static void playGame(int tabuleiroTam, int qtdBombas) {
        String bombBandeira = "";
        String bombPos      = "";
        int tabuleiro[][] = new int[tabuleiroTam][tabuleiroTam];
        for (int i = 0; i < qtdBombas; i++) {
            int j = random(tabuleiroTam, 0);
            int k = random(tabuleiroTam, 0);
            tabuleiro[j][k] = -5;
            bombPos += j + "" + k;
        }

        boolean jogFim = false;
        boolean jogadorWin = false;

        System.out.println("            Iniciando           \n");
        imprimirTabuleiroIni(tabuleiro);
        System.out.println();
        while(jogFim != true){
            char op = 'P';
            int line = 0;
            int colums = 0;
            System.out.println("P - Pisar  \tM - Marcar");
            System.out.printf("Ex: %c [linha] [coluna]\n", op);
            op = ler.next().toUpperCase().charAt(0);
            line = ler.nextInt();
            colums = ler.nextInt();

            if(line < tabuleiroTam && colums < tabuleiroTam){
                if(tabuleiro[line][colums] == -5 && op == 'P'){
                    jogFim = true;
                    jogadorWin = false;
                }else{
                    if(op == 'P'){
                        tabuleiro[line][colums] = -1;
                    }else{
                        if(tabuleiro[line][colums] != -1){
                            tabuleiro[line][colums] = -3;
                            bombBandeira += line + "" + colums;
                        }
                    }
                    imprimirTabuleiro(tabuleiro);

                    if(bombPos.equals(bombBandeira)){
                        jogFim = true;
                        jogadorWin = true;
                    }
                }
            }
            System.out.println();
        }
        System.out.println((jogadorWin == true)? "Parabéns, você ganhou!!": "Você perdeu..");
    }

    public static int random(int max, int min) {
        return (int) ((Math.random() * (max - min)) + min);
    }

    public static void imprimirTabuleiroIni(int tab[][]) {
        for (int i = 0; i < tab.length; i++) {
            for (int j = 0; j < tab.length; j++) {
                if (tab[i][j] != -1) {
                    if(tab[i][j] > 0){
                        System.out.print(tab[i][j] + " ");
                    }else{
                        System.out.print("▢ ");
                    }
                } else {
                    System.out.print("▢ ");
                }

            }
            System.out.println();
        }
    }

    public static void imprimirTabuleiro(int tab[][]) {
        System.out.println();
        for (int i = 0; i < tab.length; i++) {
            for (int j = 0; j < tab.length; j++) {
                if(tab[i][j] == -5){
                    System.out.print("▢ ");
                }else if(tab[i][j] == -3){
                     System.out.print("▣ ");
                }else if(tab[i][j] == -1){
                    System.out.print("  ");
                }else{
                    int val = verificarArredor(tab, i, j, 0);
                    System.out.print((val > 0)? val + " ": "▢ ");
                }
            }
            System.out.println();
        }
    }

    public static int[][] atrTabuleiro(int tab[][]) {
        for (int i = 0; i < tab.length; i++) {
            for (int j = 0; j < tab.length; j++) {
                if (tab[i][j] != -1) {
                     tab[i][j]= verificarArredor(tab, i, j, 0);    
                }
            }
            System.out.println();
        }
        return tab;
    }

    public static int verificarArredor(int tab[][], int i, int j, int cc) {
        if (i > 0 && i < tab.length - 1) {
            if (j > 0 && j < tab.length - 1) {
                cc += (tab[i - 1][j] == -5 ? 1 : 0) + (tab[i + 1][j] == -5 ? 1 : 0)
                        + (tab[i - 1][j - 1] == -5 ? 1 : 0) + (tab[i - 1][j + 1] == -5 ? 1 : 0)
                        + (tab[i + 1][j - 1] == -5 ? 1 : 0) + (tab[i + 1][j + 1] == -5 ? 1 : 0)
                        + (tab[i][j - 1] == -5 ? 1 : 0) + (tab[i][j + 1] == -5 ? 1 : 0);
            } else if (j == 0) {
                cc += 
                (tab[i - 1][j] == -5 ? 1 : 0) + 
                (tab[i + 1][j] == -5 ? 1 : 0)+ 
                (tab[i - 1][j + 1] == -5 ? 1 : 0) + 
                (tab[i + 1][j + 1] == -5 ? 1 : 0)+ 
                (tab[i][j + 1] == -5 ? 1 : 0);
            } else if (j == tab.length-1) {
                cc += 
                (tab[i - 1][j] == -5 ? 1 : 0) + 
                (tab[i + 1][j] == -5 ? 1 : 0)+ 
                (tab[i - 1][j - 1] == -5 ? 1 : 0) + 
                (tab[i + 1][j - 1] == -5 ? 1 : 0)+ 
                (tab[i][j - 1] == -5 ? 1 : 0);
            }
        } else {
            if (j > 0 && j < tab.length - 1) {
                if (i != tab.length - 1) {
                    cc += (tab[i + 1][j] == -5 ? 1 : 0)
                            + (tab[i + 1][j - 1] == -5 ? 1 : 0) + (tab[i + 1][j + 1] == -5 ? 1 : 0)
                            + (tab[i][j - 1] == -5 ? 1 : 0) + (tab[i][j + 1] == -5 ? 1 : 0);

                } else {
                    cc += (tab[i - 1][j] == -5 ? 1 : 0)
                            + (tab[i - 1][j - 1] == -5 ? 1 : 0) + (tab[i - 1][j + 1] == -5 ? 1 : 0)
                            + (tab[i][j - 1] == -5 ? 1 : 0) + (tab[i][j + 1] == -5 ? 1 : 0);
                }
            } else if (j == 0 && i == 0) {
                cc += (tab[i + 1][j] == -5 ? 1 : 0) +
                        (tab[i + 1][j + 1] == -5 ? 1 : 0) +
                        (tab[i][j + 1] == -5 ? 1 : 0);
            } else if (j == 0 && i == tab.length-1) {
                cc += (tab[i - 1][j] == -5 ? 1 : 0) +
                        (tab[i - 1][j + 1] == -5 ? 1 : 0) +
                        (tab[i][j + 1] == -5 ? 1 : 0);
            } else if (j == tab.length-1 && i == 0) {
                cc += (tab[i + 1][j] == -5 ? 1 : 0) +
                        (tab[i + 1][j - 1] == -5 ? 1 : 0) +
                        (tab[i][j - 1] == -5 ? 1 : 0);
            } else if (j == tab.length-1 && i == tab.length-1) {
                cc += (tab[i - 1][j] == -5 ? 1 : 0) +
                        (tab[i - 1][j - 1] == -5 ? 1 : 0) +
                        (tab[i][j - 1] == -5 ? 1 : 0);
            }
        }
        return cc;
    }
}
