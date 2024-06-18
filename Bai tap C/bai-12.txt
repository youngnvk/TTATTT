
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define true 1
#define false 0
int a[1000];
void khoitao(int n)
{
    for(int i=1; i<=n; i++)
    {
        a[i]=0;
    }
    a[1]=1;
}
int laSNT(int n)
{
    int a[1000];
    for(int i=1; i<=n; i++)
    {
        a[i]=0;
    }
    a[1]=1;
    for(int i=2; i<=sqrt(n); i++)
    {
        if(a[i]==0)
        {
            for(int j=i*i; j<=n; j+=i)
            {
                a[j]=1;
            }
        }
    }
    if(a[n]==0)
    {
        return true;
    }
    return false;

}
void sang(int b[],int n)
{
    int dem=1;
    for(int i=2; i<=n; i++)
    {
        if(a[i]==0)
        {
            for(int j=i*i; j<=n; j=j+i)
            {
                a[j]=1;
            }

        }
        if(a[i]==0)
            {
                b[dem]=i;
                dem++;

            }

    }
    int i=0;
    int sum=0;
    while(i+4<dem)
    {
        sum=b[i+1]+b[i+2]+b[i+3]+b[i+4];
        if(laSNT(sum)==true && sum<=n)
        {
            printf("(%d ,%d ,%d ,%d) ",b[i+1],b[i+2],b[i+3],b[i+4]);
        }
        i++;
    }

}
int main()
{
    int n;
    int b[1000];
    scanf("%d",&n);
    khoitao(n);
    sang(b,n);
}
