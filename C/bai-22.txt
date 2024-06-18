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
int F(int n)
{
    if(laSNT(n)==true)
    {
	return n;
    }
    return 0;
}
void tinhtong(int l,int r)
{
    int tong=0;
    for(int i=l;i<r;i++)
    {
        for(int j=i+1;j<=r;j++)
        {
            tong=tong+F(i)*F(j);
        }
    }
    printf("%d",tong);
}
int main()
{
    int l,r;
    scanf("%d%d",&l,&r);
    tinhtong(l,r);
}
