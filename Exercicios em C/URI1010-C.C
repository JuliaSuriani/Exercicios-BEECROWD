#include <stdio.h>

int main() {

     int CP1, Q1, CP2, Q2;
    float V1, V2, total;
    scanf ("%d%d%f",&CP1,&Q1,&V1);
    scanf ("%d%d%f", &CP2,&Q2,&V2);
    total = (Q1*V1)+(Q2*V2);
    printf ("VALOR A PAGAR: R$ %.2f\n",total);

    return 0;
}