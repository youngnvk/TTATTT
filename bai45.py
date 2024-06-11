import math
import random

def phantich(n):
    x = n - 1
    s = 0
    while x % 2 == 0:
        s += 1
        x //= 2
    r = x
    return s, r

import random

def modulo(a, k, n): #nhan binh phuong co lap
    b = 1
    A = a
    while k != 0:
        if k % 2 != 0:
            b = (b * A) % n
        A = (A * A) % n
        k = k // 2
    return b

def phantich(n):
    x = n - 1
    s = 0
    while x % 2 == 0:
        s += 1
        x = x // 2
    r = x
    return s, r

def miller(n, t):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s, r = phantich(n)
    for i in range(t):
        a = random.randint(2, n - 2)
        y = modulo(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = modulo(y, 2, n)
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True

if __name__ == '__main__':
    t = int(input('Nhập số lần lặp: '))
    while True:
        n = int(input('Nhập N: '))
        if 0 < n < 1000:
            break
        else:
            print('Mời bạn nhập lại!')

    p = int(input('Nhập p: '))

    ok = False
    for a in range(n + 1):  # Thêm 1 để kiểm tra cả giá trị a = 0
        a_value = a
        k = modulo(a_value, p, n)
        if miller(k, t) == True:
            print(f"a = {a_value}, thỏa mãn {a_value} ^ {p} % {n} là số nguyên tố")
            print('')
            ok = True
    if not ok:
        print('Không có số nào thỏa mãn!')


def miller(n, t):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s, r = phantich(n)
    for i in range(t):
        a = random.randint(2, n - 2)
        y = modulo(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = modulo(y, 2, n)
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True

def distance(A):
    min_distance = 10000000  
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            k = abs(A[i] - A[j])
            if min_distance > k:
                min_distance = k
    return min_distance
def list_primes(start, end, t, n):
    primes = []
    cnt = 0
    for i in range(start, end + 1):
        if cnt == n:
            break
        if miller(i, t):
            cnt += 1
            primes.append(i)    
    return primes
if __name__ == '__main__':
    n = int(input('Nhap n la so luong phan tu cua mang: '))
    t = int(input('Nhap so lan lap: '))
    A = list_primes(2, 100000, t, n)
    print(f'Mang A chua {n} so nguyen to: {A}')
    print(f'Khoang cach ngan nhat cua 2 so bat ky trong mang A la: {distance(A)}')
