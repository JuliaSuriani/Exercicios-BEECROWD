#include <stdio.h>
 
int main()
{
    double area, raio;
    area = 0.0;
    raio = 0.0;
    scanf ("%lf",&raio );
    area = 3.14159 * (raio * raio);
    printf("A=%.4lf\n",area);
 
    return 0;
}