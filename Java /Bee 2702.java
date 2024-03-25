/*
Entrada
A primeira linha contem três inteiros Ca, Ba e Pa (0 ≤ Ca, Ba, Pa ≤ 100), representando respectivamente o número de refeições disponiveis de frango, bife e massa. A segunda linha contem três inteiros Cr, Br e Pr (0 ≤ Cr, Br, Pr ≤ 100), indicando respectivamente o número de refeições requisitadas de frango, bife e massa respectivamente.

Saída
Imprima uma única linha com um inteiro representando o número de passageiros que seguramente não receberão sua escolha de refeição.
*/
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    // disponiveis
    int Ca = scan.nextInt();
    int Ba = scan.nextInt();
    int Pa = scan.nextInt();
    // requisitados
    int Cr = scan.nextInt();
    int Br = scan.nextInt();
    int Pr = scan.nextInt();

    int total = Math.max(0, Cr - Ca) + Math.max(0, Br - Ba) + Math.max(0, Pr - Pa);
    System.out.println(total);
  }
}
