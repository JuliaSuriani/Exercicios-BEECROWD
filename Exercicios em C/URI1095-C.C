#include<stdio.h>
int main() {
int N1,N2;
N1=1;
N2=60;

for(N1=1,N2=60;N2<=60;N1+=3,N2-=5)
{
  printf("I=%d J=%d\n",N1,N2);
if (N2==0)
    break;

}

return 0;
}