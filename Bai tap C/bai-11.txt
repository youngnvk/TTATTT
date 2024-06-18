
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
int a[1000];
void khoitao(int n)
{
    for(int i=1;i<=n;i++)
    {
        a[i]=0;
    }
    a[1]=1;
}

void sang(int n)
{
    int dem=0;
    for(int i=2;i<=n;i++)
    {
        if(a[i]==0)
        {
            for(int j=i*i;j<=n;j=j+i)
            {
                a[j]=1;
            }
        }
        if(a[i]==0)
        {
            dem=dem+i;
        }

    }
    printf("tongSNT:%d\n", dem);
}
int main()
{
    int n;
    scanf("%d",&n);
    sang(n);
}
