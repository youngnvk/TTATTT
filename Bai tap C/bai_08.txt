#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

void xuli(int n)
{
    for(int i=4;i<=n;i++)
    {
        int dem=0;
        for(int j=2;j<=i/2;j++)
        {
            if(i%j==0)
            {
                dem++;
            }
        }
        if(dem==1)
        {
            printf("%d ",i);
        }
    }
}
int main()
{
    int n;
    scanf("%d",&n);
    xuli(n);
}
