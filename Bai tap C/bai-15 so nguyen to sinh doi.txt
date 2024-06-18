
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
void sang(int n)
{
    int dem=1;
    for (int i=2; i<=n; i++)
    {
        if(a[i]==0)// neu a[i] la SNT thi moi thuc hien vi neu thuc hien tat ca se gan 1 trung lap voi cac lan gan truoc do
        {
            for(int j=i*i; j<=n; j+=i)
            {
                a[j]=1;
            }
        }
        if(a[i]==0)
        {
            b[dem++]=i;
        }

    }
    for(int i=1;i<=dem-1;i++)
    {
        if(b[i+1]-b[i]==2)
        {
            printf("(%d,%d)",b[i],b[i+1]);
        }
    }
}
int main()
{
    int n;
    scanf("%d",&n);
    khoitao(n);
    sang(n);

}
