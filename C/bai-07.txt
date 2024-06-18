#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define true 1
#define false 0
int a[10000];
void khoitao(int n)
{
    for(int i=1; i<=n; i++)
    {
        a[i]=0;
    }
    a[1]=1;
}
void sang(int n)
{
    for(int i=2; i<=n; i++)
    {
        if(a[i]==0)
        {
            for(int p=i*i; p<=n; p+=i)
            {
                a[p]=1;
            }
        }
    }
}
int daonguoc(int n)
{
    int k=log10(n)+1;
    int p=0;
    for(int i=k-1; i>=0; i--)
    {
        int x=n%10;
        p=p+x*pow(10,i);
        n=n/10;
    }
    return p;
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
void xuli(int n)
{
    for(int i=1; i<=n; i++)
    {
        if(a[i]==0)
        {
            if(laSNT(daonguoc(i))==true)
            {
                printf("%d ",i);
            }
        }
    }
}
int main()
{
    int n;
    scanf("%d",&n);
    khoitao(n);
    sang(n);
    xuli(n);
}
