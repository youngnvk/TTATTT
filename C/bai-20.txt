
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define true 1
#define false 0
#include <time.h>
int gcd(int a,int b)
{
    while(b!=0)
    {
       int r=a%b;
        a=b;
        b=r;
    }
    return a;

}
void xuli(int m,int n,int d)
{
    for(int i=m;i<=n;i++)
    {
        for(int j=i+1;j<=n;j++)
        {
            if(gcd(j,i)==d)
            {
                printf("(%d,%d) ",i,j);
            }
        }
    }
}
int main()
{
    int m,n,d;
    scanf("%d%d%d",&m,&n,&d);
    xuli(m,n,d);
}
