#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void tonguoc(int sum1[],int n)
{
    for(int i=1;i<=n;i++)
    {
        int sum=0;
        for (int j=1;j<i;j++)
        {
            if(i%j==0)
            {
                sum=sum+j;
            }
        }
        sum1[i]=sum;
    }
}
void capsothanthiet(int sum1[],int n)
{
    for(int i=1;i<=n;i++)
    {
        int k=sum1[i];
        if(i<sum1[i] && sum1[i]<=n&&sum1[k]==i)
        {
            printf("(%d,%d) ",i,sum1[i]);
        }
    }
}
int main()
{
    int n;
    int sum[10000];
    scanf("%d",&n);
    tonguoc(sum,n);
    capsothanthiet(sum,n);
}
