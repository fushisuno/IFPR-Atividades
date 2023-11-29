package Ordenação;

public class SelectionSort {
  public static void main(String[] args){
    int vet[] = {94, 2, 27, 3, 32, 46, 8, 0};
    vet = selectionSort(vet);
  }


  public static int[] selectionSort(int vet[]){
    int menor = 0, menor_pos = 0, aux = 0;
  
    for (int i = 0; i < vet.length-1; i++) {
      menor = vet[i];
      for (int j = i+1; j < vet.length; j++) {
        if(vet[j] < menor){
          menor = vet[j];
          menor_pos = j;
        }
      }
        int opo = vet[menor_pos];
        vet[menor_pos] = vet[i];
        vet[i] = opo;
      
    }
    return vet;
  }
}
