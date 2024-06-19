
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define true 1
#define false 0
int a[1000],b[1000];
void khoitao(int n)
{
    for(int i=1; i<=n; i++)
    {
        a[i]=0;
    }
    a[1]=1;
}
int sang(int n)
{
    int dem=1;
    for (int i=2; i<=n; i++)
    {
        if(!a[i])
        {
            for(int j=i*i; j<=n; j=j+i)
            {
                a[j]=1;
            }
            if(a[i]==0)
            {
                b[dem++]=i;
            }
        }

    }

    return dem;
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
void timtonghieuSNT(int n,int m)
{
    for (int i=1;i<=n;i++)
    {
        for(int j=i+1;j<=n;j++)
        {
            if(b[i]+b[j] <= m && laSNT(b[i]+b[j])==true  && laSNT(b[j]-b[i])==true)
            {
                printf("(%d,%d) ",b[i],b[j]);
            }
        }
    }
}
int main()
{
   int n;
   scanf("%d",&n);
   khoitao(n);
   int dem=sang(n);
   timtonghieuSNT(dem,n);
}
