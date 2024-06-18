
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define true 1
#define false 0
#include <time.h>
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
void khoitao(int a[],int n)
{
    for(int i=1; i<=n-1; i++)
    {
        a[i]=0;
    }
    a[1]=1;
}
int lasieuNT(int n)
{
    int a[1000];
    khoitao(a,n);
    int dem=0;
    for(int i=2; i<=n-1; i++)
    {
        if(a[i]==0)
        {
            for(int j=i*i; j<=n-1; j=j+i)
            {
                a[j]=1;
            }
        }
        if(a[i]==0)
        {
            dem++;
        }

    }
    if(laSNT(dem)==true)
    {
       return true;
    }
    return false;
}
int main()
{
    int a,b;
    scanf("%d%d",&a,&b);
    for(int i=a;i<=b;i++)
    {
        if(lasieuNT(i)==true)
        {
            printf("%d ",i);
        }
    }
}
