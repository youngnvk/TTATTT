import math
def gcd(a, b):
    A = a
    B = b
    while(B > 0):
        R = A % B
        A = B
        B = R
    return A
def nto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
if __name__=='__main__':
    n = int(input('Nhập số lượng phần tử: '))
    # Nhập mảng từ bàn phím
    arr = [0] * (n)
    for i in range(n):
        arr[i] = int(input(f'Nhập phần tử mảng thứ {i} là : '))
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if nto(gcd(arr[i], arr[j])):
                cnt += 1
    print(f'tổng số cặp thỏa mãn là : {cnt}')