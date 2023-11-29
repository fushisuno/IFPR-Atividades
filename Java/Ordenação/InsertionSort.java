package Ordenação;

public class InsertionSort {
  public static void main(String[] args){
    int vet[] = {94, 27, 32, 46, 8, 0};
    vet = insertionSort(vet);
  }


  public static int[] insertionSort(int vet[]){
    int aux = 0;
    for (int i = 1; i < vet.length; i++) {
      aux = i;
      while(aux > 0 && vet[aux] < vet[aux-1]){
          int opo = vet[aux-1];
          vet[aux-1] = vet[aux];
          vet[aux] = opo;
          aux--;
      }
    }
    return vet;
  }
}
