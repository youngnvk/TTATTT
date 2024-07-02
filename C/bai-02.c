#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int max(int a,int b)
{
    return a>b?a:b;
}
void khoitao(int a[],int left,int right)
{
    int n=right-left+1;
    for (int i=0;i<=n;i++)
    {
       a[i]=0;
    }
}
void sang(int a[],int left,int right)
{
    int n=right-left+1;
    for (int i=2;i<=sqrt(right);i++)
    {
        for(int p=max(i*i,(left+i-1)/i*i);p<=right;p=p+i)
        {
            a[p-left]=1;
        }
    }
   for(int i=max(left,2);i<=right;i++)
    {
        if(a[i-left]==0)
        {
            printf("%d ",i);
        }
    }

}
int main()
{
    int a[1000];
    int n;
    scanf("%d",&n);

    int left=pow(10,n-1);
    int right=pow(10,n)-1;
    khoitao(a,left,right);
    sang(a,left,right);

}
