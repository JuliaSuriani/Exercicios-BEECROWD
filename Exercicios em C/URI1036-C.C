#include <stdio.h>
#include <math.h>

int main() {
 double A,B,C,D;
 scanf("%lf%lf%lf",&A,&B,&C);

 if (((B*B)-4 *A *C)<0||A==0) {
     printf("Impossivel calcular\n");

 }
else {
    D = sqrt((B*B)-4*A*C);
    printf ("R1 = %.5lf\nR2 = %.5lf\n",((-B + D)/(2 * A)),((-B-D)/(2*A)));
}

    return 0;
}