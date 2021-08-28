#include <stdio.h>
#include <stdlib.h>
int main ()
{
    int *T,C,i;
    T= NULL;
    char s[10000];
    scanf("%d",&T);
    for(i=1;i<=T;i++){
        scanf("%s",&s);
        C =strlen(s);
        printf("%.2f\n",C/100.0);
    }

return 0;
}
