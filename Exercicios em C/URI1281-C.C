#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct TipoFruta
{
    char nome[51];
    double valor;
};
int main()
{
    struct TipoFruta *pointer;
    int i, j, k, teste, teste_p1, teste_p2, quant;
    char nome[51];
    double total;
    scanf("%d", &teste);
    for (i=0; i<teste; i++)
        {
          scanf("%d", &teste_p1);
                pointer = (struct TipoFruta *) calloc (sizeof(struct TipoFruta), teste_p1);
          for (j=0; j<teste_p1; j++)
             {
                      scanf ("%s%lf", pointer[j].nome, &pointer[j].valor);
             }
          scanf("%d", &teste_p2);
          total = 0;
          for (j=0; j<teste_p2; j++)
                {
                  scanf ("%s%d",nome, &quant);
                  for (k=0; k<teste_p1; k++)
                            {
                            if (strcmp (nome, pointer[k].nome) == 0)
                                    total = (pointer[k].valor) * (quant) + total;
                            }
                }
    printf ("R$ %.2lf\n", total);
    free (pointer);
        }
    return 0;
}
