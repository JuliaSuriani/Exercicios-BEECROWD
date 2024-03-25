/*
Escreva um programa que, dado um registro de log, este seja convertido em textos mais legíveis.
Entrada
A primeira linha contém a quantidade de casos de teste. Cada linha de um caso de teste possui três inteiros H, M e O,
sendo a hora, o minuto da ocorrência, e a própria ocorrência (zero se a porta fechou ou um se a porta abriu).
Saída
Para cada caso de teste, imprima o horário da ocorrência, no devido formato, seguido de um espaço, um hífen e um espaço, 
e da frase “A porta abriu!” ou “A porta fechou!”, conforme a ocorrência registrada.
*/

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int entrada = 0;

    entrada = scan.nextInt();
    for (int i = 0; i < entrada; i++) {
      int H = scan.nextInt();
      int M = scan.nextInt();
      int O = scan.nextInt();
      if (O == 0) {
        System.out.printf("%02d:%02d - A porta fechou!%n", H, M);
      } else if (O == 1) {
        System.out.printf("%02d:%02d - A porta abriu!%n", H, M);
      }
    }
  }
} 
