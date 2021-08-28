#include <stdio.h>
int main()
{
    int A,B,C,D,X,Y;
    while(1)
    {
        scanf("%d", &A);
        if(A==0) break;
        else
        {
            scanf("%d%d", &B,&C);
            D = A*B;
            X = (D*100)/C;
            Y = pow(X,.5);
            printf("%d\n",Y);
        }
    }
    return 0;
}
