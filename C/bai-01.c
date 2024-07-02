#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define true 1
#define false 0
int laQprime(int a)
{
    int dem=0;
    for(int i=2;i<= a/2;i++)
    {
        if(a%i==0)
        {
            dem++;
        }
    }
    if(dem==2)
    {
        return true;
    }
    else
    {
        return false;
    }
}
void cacsoQprime(int n)
{
    for(int i=n;i>=1;i--)
    {
        if(laQprime(i)==true)
        {
            printf("%d  ",i);
        }
    }
}
int main()
{
    int n;
    scanf("%d",&n);
    cacsoQprime(n);
}
