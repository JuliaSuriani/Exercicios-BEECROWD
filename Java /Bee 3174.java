/*
Entrada
O primeiro valor da entrada é um valor inteiro N (1 ≤ N ≤ 1000), indicando a quantidade de elfos que o Papai Noel contratou. 
As N linhas seguintes possuem três valores E, G e H (1 ≤ H ≤ 24), indicando respectivamente o nome do elfo, 
em qual grupo ele vai trabalhar (em letras minúsculas) e quantas horas por dia ele irá ajudar (em valor inteiro).

Saída
A saída deverá ser um inteiro P, a quantidade total de presentes produzida por dia pela fábrica do Papai Noel.
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int b = 0, a = 0, m = 0, d = 0;
        int n = scan.nextInt();

        for (int i = 0; i < n; i++) {
            String elfoNome = scan.next();
            String grupo = scan.next();
            int horas = scan.nextInt();

            if (grupo.equals("bonecos")) {
                b += horas;
            } else if (grupo.equals("arquitetos")) {
                a += horas;
            } else if (grupo.equals("musicos")) {
                m += horas;
            } else if (grupo.equals("desenhistas")) {
                d += horas;
            }
        }

        a = a / 4;
        b = b / 8;
        d = d / 12;
        m = m / 6;

        int totalPresentes = a + b + d + m;
        System.out.println(totalPresentes);
    }
}
