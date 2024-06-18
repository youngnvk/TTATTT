#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define true 1
#define false 0
#include <time.h>
int random(int min,int max)
{
    return min+rand()%(max-min+1);
}
void sinhMang(int a[],int n)
{
    for(int i=0;i<n;i++)
    {
        a[i]=random(1,n);
    }
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
void xuli(int a[],int n)
{
    for(int i=0;i<n;i++)
    {
        if(laSNT(a[i])==true)
        {
            printf("%d ",a[i]);
        }
    }
}
void inMang(int a[],int n)
{
  for(int i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }

}

int main()
{
    int a[1000],n;
    srand(time(NULL));
    scanf("%d",&n);
    sinhMang(a,n);

    inMang(a,n);
       printf("\n");
    xuli(a,n);

}
