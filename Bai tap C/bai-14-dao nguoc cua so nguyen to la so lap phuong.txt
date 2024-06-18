
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define true 1
#define false 0
int a[1000],b[1000];
void khoitao(int l,int r)
{
    for(int i=1; i<=r-l+1; i++)
    {
        a[i]=0;
    }
    a[1]=1;
}
int max(int a,int b)
{
    return a>=b?a:b;
}
void sangtrendoan(int l,int r)
{
    for (int i=2;i<=r;i++)
    {
        for(int j=max(i*i,(l+i-1)/i*i);j<=r;j+=i)
        {
            if(a[j-l+1]==0)
            {
                a[j-l+1]=1;
            }
        }
    }
}
int kiemtralapphuong(int n)
{
    double canbac3=cbrt(n);
    if(fabs(canbac3-round(canbac3))==0.00000)
        return true;
    return false;
}
int daonguoc(int n)
{
    int k=log10(n)+1;
    int sum=0;
    for(int i=k-1;i>=0;i--)
    {
        sum=sum+(n%10)*pow(10,i);
        n=n/10;
    }
    return sum;
}
void solapphuong(int sochuso)
{
    int l=pow(10,sochuso-1);
    int r=pow(10,sochuso)-1;
    sangtrendoan(l,r);
    for(int i=1;i<=r-l+1;i++)
    {
        if(a[i]==0&&kiemtralapphuong(daonguoc(i+l-1))==true)
        {
            printf("dao nguoc cua %d la %d la so lap phuong\n",i+l-1,daonguoc(i+l-1));
        }
    }
}
int main()
{
  int n;
  printf("Nhap so chu so: ");
  scanf("%d",&n);
  solapphuong(n);
}
