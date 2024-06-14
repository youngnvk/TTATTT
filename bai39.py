
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
    input1 = input('Nhập các số : ')
    # Nhập mảng từ bàn phím
    array = list(map(int, input1.split()))
    cnt = 1
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if nto(gcd(array[i], array[j])):
                print(f'cặp số thứ {cnt} ({array[i]}, {array[j]})')
                cnt += 1
