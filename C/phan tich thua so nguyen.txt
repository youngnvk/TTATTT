#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void khoitao(int a[],int l,int r)
{
    for (int i=0;i<r-l+1;i++)
    {
        a[i]=0;
    }
}
int max(int a,int b)
{
    return a>=b?a:b;
}
void xuli(int a[],int l,int r)
{
    int n=r-l+1;
    for(int i=2;i<=sqrt(r);i++)
    {
        for(int p=max(i*i,(l+i-1)/i*i);p<=r;p+=i)
        {
            a[p-l]=1;
        }
    }
    int sum=0;
    for(int i=0;i<n;i++)
    {
        if(a[i]==0&&i+l>1)
        {
            printf("%d ",i+l);
            sum=sum+i+l;
        }
    }

    printf("\n%d", sum);
}
int main()
{
    int a[1000];
    int l,r;
    scanf("%d%d",&l,&r);
    khoitao(a,l,r);
    xuli(a,l,r);
}
