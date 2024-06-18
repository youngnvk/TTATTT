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
int f(int a,int b,int c,int x)
{
    return a*x*x+b*x+c;
}

void xuli(int a,int b,int c)
{
    int i=1;
    while(laSNT(f(a,b,c,i))==false)
    {
        i++;
    }
    printf("x=%d",i);
}


int main()
{
    int a,b,c;
    scanf("%d%d%d",&a,&b,&c);
    xuli(a,b,c);

}
