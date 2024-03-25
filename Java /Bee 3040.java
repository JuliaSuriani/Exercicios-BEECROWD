/* Entrada
A primeira linha de entrada contém um inteiro N (0 < N ≤ 10000), o número de casos teste.
As N linhas seguintes contém 3 inteiros cada, h, de g (0 < a, d, g ≤ 5000), 
a altura da árvore em centímetros, o seu diâmetro em centímetros, e a quantidade de galhos da árvore.

Saída
Sua tarefa é, para cada árvore, imprimir Sim, se ela é uma árvore que Roberto pode escolher, ou Não, se é uma árvore que ele não deve escolher.
*/

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int N = 0;
    int h, d, g = 0;
    N = scan.nextInt();
    for (int i = 0; i < N; i++) {
      h = scan.nextInt();
      d = scan.nextInt();
      g = scan.nextInt();
      if (h >= 200 && h <= 300 && d >= 50 && g >= 150) {
        System.out.println("Sim");
      } else {
        System.out.println("Nao");
      }
    }
  }
}
