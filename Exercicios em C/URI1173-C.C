#include <stdio.h>

int main() {

   int V, i, J[10];
    scanf("%d",&V);
    if(V<50)
    {
        for(i=0; i<10; i++)
        {
            J[i] = V;
            printf("N[%d] = %d\n",i,V);
            V*=2;
        }
    }

    return 0;
}