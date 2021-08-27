#include <stdio.h>

int main()
 {
 float S; //s = salário
 scanf("%f", &S);

 if (S <= 2000.0)
 {
      printf("Isento\n");
 }
  else if (S <= 3000.0)
     printf("R$ %.2f\n", (S - 2000.0) * 0.08);
  else if (S <= 4500.0)
    printf("R$ %.2f\n", 1000.0 * 0.08 + (S - 3000.0) * 0.18);
 else
 {
    printf("R$ %.2f\n", 1000.0 * 0.08 + 1500.0 * 0.18 + (S - 4500.0) * 0.28);
 }
return 0;
}