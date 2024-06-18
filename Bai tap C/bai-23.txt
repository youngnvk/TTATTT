#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define true 1
#define false 0
#include <time.h>
/*
int F(int n)
{
    if(n<=1)
    {
        return false;
    }
    for(int i=2; i<=sqrt(n); i++)
    {
        if(n%i==0)
            return false;
    }
    return true;
}*/
void khoitao(int a[],int l,int r)
{
    for(int i=1;i<=r-l+1;i++)
        a[i]=0;
}
int max(int a,int b)
{
    return a>=b?a:b;
}
void sangtrendoan(int a[],int l,int r)
{
    int sum=0;
    for (int i=2;i<=r;i++)
    {
        if(a[i]==0)
        {
            for (int j=max(i*i,(l-i+1)/i*i);j<=r;j+=i)
            {
                a[j-l+1]=1;
            }
        }
    }
    for(int i=1;i<=r-l+1;i++)
    {
        if(a[i]==0&&i+l-1>1)
        {
            sum=sum+i+l-1;
        }
    }
     printf("%d\n",sum);
    if(F(sum)==true)
    {
        printf("yes");
    }
    else
    {
        printf("no");
    }
}
int main()
{
    int a[1000],l,r;
    scanf("%d%d",&l,&r);
    khoitao(a,l,r);
    sangtrendoan(a,l,r);

}
