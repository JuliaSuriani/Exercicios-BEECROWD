/*
Escreva um programa que leia um valor inteiro N (1 < N < 1000). Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.
*/
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int N = 0;
    int i = 1;
    N = scan.nextInt();
    while (i <= N) {
      double aoQuadrado, aoCubo = 0;
      aoQuadrado = i * i;
      aoCubo = Math.pow(i, 3);
      System.out.printf("%d %.0f %.0f\n", i, aoQuadrado, aoCubo);
      i = i + 1;
    }
  }
}
