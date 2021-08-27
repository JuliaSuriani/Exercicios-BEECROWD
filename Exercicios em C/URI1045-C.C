#include <stdio.h>

int main()
{
 float A, B, C, H;
 scanf("%f %f %f", &A, &B, &C);
  if (A < B){ H = A; A = B; B = H; }
  if (B < C){ H = B; B = C; C = H; }
  if (A < B){ H = A; A = B; B = H; }
  if (A >= B + C) printf("NAO FORMA TRIANGULO\n");
     else
  if (A*A == B*B + C*C)
      printf("TRIANGULO RETANGULO\n");
     else
  if (A*A > B*B + C*C)
  {
  printf("TRIANGULO OBTUSANGULO\n");
  }
   else
     if (A*A < B*B + C*C)
        printf("TRIANGULO ACUTANGULO\n");
     if (A==B && B==C)
        printf("TRIANGULO EQUILATERO\n");
    else
     if (A==B || B==C)
        printf("TRIANGULO ISOSCELES\n");

return 0;
}
