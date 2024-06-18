
#include<stdio.h>
#include<math.h>
#include<windows.h>

void inmang(int a[],int p,int w,int t)
{
    for(int i = t-1; i>=0; i--)
        printf("%5d",a[i]);
    printf("\n");
}

void phanTichThanhMang(int a[],int n,int p,int w,int t)
{
    int tmpAr[4];
    for(int i = 3 ; i >=0 ; i --)
    {
        int tmp = (int)pow(2,(i*w));
        tmpAr[i] = (int)n/tmp;
        n -=tmpAr[i]*tmp;
    }
    for(int i = 0 ; i < 4 ; i ++)
    {
        a[i] = tmpAr[3-i];
    }
}

int chuyenMangThanhSo(int a[],int p,int w,int t)
{
    int n=0;
    for(int i = t-1; i >=0 ; i --)
    {
        n+=pow(2,i*w)*a[3-i];
    }
    return n;
}

int mod(int n,int p,int w,int t)
{
    if (n < 0)
    {
        return (int) (pow(2, w) + n);
    }
    else
        return  n % (int)(pow(2, w));
}

int congCSB(int a[], int b[],int c[],int p,int w,int t)
{
    int esi=0;
    for(int i = t-1; i >=0 ; i --)
    {
        int tmp= a[i]+b[i]+esi;
        esi =  ((tmp >= 0 && tmp <pow(2, w)) ? 0 : 1);
        c[i] = mod(tmp,p,w,t);
    }
    return esi;
}

void truCSB(int a[], int b[],int c[],int p,int w,int t )
{
    int esi=0;
    for(int i = t-1 ; i >=0 ; i --)
    {
        int tmp= a[i]-b[i]-esi;
        esi =  ((tmp >= 0 && tmp <pow(2, w)) ? 0 : 1);
        c[i] = mod(tmp,p,w,t);
    }
}

int isPrime(int n)
{
    int a[1000];
    for(int i=1; i<=n; i++)
    {
        a[i]=0;
    }
    a[1]=1;
    for (int i=2; i<=sqrt(n); i++)
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
        return 1;
    }
    return 0;
}

int main()
{
    int number1,number2;

    int p,m,t,w=8;
    printf("nhap so p");
    do
    {
        scanf("%d",&p);
    }
    while(!isPrime(p));
    m = (int)log2(p)+1;
    t = (int)(m/w)+1;
    int a [t] ;
    int b [t];
    int CCSB [t];
    int TCSB [t];
    int pARR[t];
    printf("nhap so a b can tinh \n");
    scanf("%d%d",&number1,&number2);
    phanTichThanhMang(a,number1,p,w,t);
    phanTichThanhMang(b,number2,p,w,t);
    phanTichThanhMang(pARR,p,p,w,t);
    // yeu cau 1
    inmang(pARR,p,w,t);
    //yeu cau 2
    int esi= congCSB(a,b,CCSB,p,w,t);
    inmang(CCSB,p,w,t);
    printf("bit nho %d\n",esi);
    //yeu cau 3
    printf("cong tren truowng fp");
    if(esi == 1)
    {
        truCSB(CCSB,pARR,TCSB,p,w,t);
        inmang(TCSB,p,w,t);
        printf("%d",chuyenMangThanhSo(TCSB,p,w,t));
    }
    else
    {
        int tmp1= chuyenMangThanhSo(CCSB,p,w,t);
        int tmp2= chuyenMangThanhSo(pARR,p,w,t);

        if(tmp1>tmp2)
        {
            truCSB(CCSB,pARR,TCSB,p,w,t);
            inmang(TCSB,p,w,t);
            printf("%d",chuyenMangThanhSo(TCSB,p,w,t));
        }
        else
        {
            inmang(CCSB,p,w,t);
            printf("%d",chuyenMangThanhSo(CCSB,p,w,t));
        }
    }
}
