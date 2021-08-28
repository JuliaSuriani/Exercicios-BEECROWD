#include <stdio.h>
#include <stdlib.h>
int main ()
{ int *n, m;
n = NULL;
    char temp[10];
    scanf("%d %d", &n, &m);
    int cnt = n;
    while(m--)
    {
        scanf("%s", temp);
        if(temp[0] == 'f') cnt++;
        else cnt--;
    }
    printf("%d\n", cnt);

return 0;
}
