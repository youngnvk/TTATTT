#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void khoitao(int a[],int n)
{
    for (int i=2;i<=n;i++)
    {
        a[i]=0;
    }
}
void sang(int a[],int n)
{

    for (int i=2;i<=n;i++)
    {
        for(int p=i*i;p<=n;p+=i)
        {
            a[p]=1;
        }
    }

}
void tinhtoan(int a[],int n)
{
    int k=0;
    int q=0;
    int p=0;
    int s=0;
    for(int i=1;i<=n;i++)
    {
        if(a[i]==0&&n%i==0&&i!=1)
        {
            k++;
            q=q+i;
        }
        if(n%i==0)
        {
           p=p+i;
           s++;

        }
    }
    printf("%d",n+p+s-q-k);
}
int main()
{
    int n;
    int a[1000];
    scanf("%d",&n);
    khoitao(a,n);
    sang(a,n);
    tinhtoan(a,n);
}
