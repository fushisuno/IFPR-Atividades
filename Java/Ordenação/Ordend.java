package Ordenação;

import java.util.Scanner;

public class Ordend {
  static Scanner ler = new Scanner(System.in);

  public static void main(String[] args) {
    int tamanhoVetorA = 0;
    int vetA[] = { 15, 19, 28 };
    int[] vetB = { 14, 16, 30, 35 };
    mergingSort(vetA, vetB);
  }

  public static int[] lerVetor(int vet[]) {
    for (int i = 0; i < vet.length; i++) {
      vet[i] = ler.nextInt();
    }
    return vet;
  }

  public static void mergingSort(int vetA[], int vetB[]) {
    // if(vetA.length == 0) return vetA;
    // if(vetA.length == 0) return vetA;
    int vetC[] = new int[vetA.length + vetB.length];
    int contA = 0, contB = 0;

    for (int j = 0; j < vetC.length; j++) {
      if (contA < vetA.length && contB < vetB.length - 1) {
        if (vetA[contA] < vetB[contB]) {
          vetC[j] = vetA[contA];
          contA++;
        } else {
          vetC[j] = vetB[contB];
          contB++;
        }
      }else{
        if(contA >= vetA.length){
          vetC[j] = vetB[contB];
          contB++;
        }else if(contB >= vetB.length){
          vetC[j] = vetA[contA];
          contA++;
        }
      }
    }
    imprimirVetor(vetC);
    // return vetC;
  }


    public static int[] imprimirVetor(int vet[]) {
    System.out.print('[');
    for (int i = 0; i < vet.length; i++) {
      if(i<vet.length-1){
        System.out.print(vet[i] + ", ");
      }else{
        System.out.print(vet[i] + "]");
      }
    }
    System.out.println();
    return vet;
  }

}
