/*
Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Entrada
A entrada contém um valor inteiro N (0 < N < 13).

Saída
A saída contém um valor inteiro, correspondente ao fatorial de N.
*/
import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    int N = 0;
    int fatorial = 1;
    Scanner scan = new Scanner(System.in);
    N = scan.nextInt();
    for (int i = 1; i <= N; i++) {
      fatorial *= i;
    }
    System.out.println(fatorial);
  }
}
