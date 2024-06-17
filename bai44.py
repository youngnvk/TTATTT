import math
def gcd(a, b):
    A = a 
    B = b 
    while(B > 0):
        R = A % B
        A = B
        B = R
    return A
def nghichdao(a, p):
    if gcd(a, p) != 1: #dieu kien nghich dao
        return False
    u = a 
    v = p
    x1 = 1
    x2 = 0
    if u == 0: #dieu kieu chia 0
        return False
    while(u != 1):
        q = v // u
        r = v - q * u
        x = x2 - q * x1
        v = u
        u = r
        x2 = x1
        x1 = x
    return x1 % p
if __name__=='__main__':
    A = []
    n = int(input('Nhap vao so phan tu trong mang A : '))
    for i in range(n):
        k = int(input(f'Nhap gia tri cua phan tu thu {i}: '))
        A.append(k)
    p = int(input('Nhap gia tri cua p: '))
    B = []
    for i in range(n):
        r = nghichdao(A[i], p)
        if r == False:
            print(f'Không thể tìm nghịch đảo cho phần tử thứ {i}: {A[i]} với p = {p}')
            break
        B.append(r)
    if len(B) == n:
        print('Mảng B có các phần tử là nghịch đảo của các phần tử tương ứng trong A:')
        print(f'B = {B}')
# A = [5, 7, 11, 13, 3, 23]
# p = 2
