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

def bin(n):
    arr = []
    cnt = 0
    while(n != 0):
        r = n % 2
        arr.append(r)
        cnt += 1
        n //= 2  # Thay đổi n / 2 thành n // 2
    return cnt, arr

def nhanbinhphuongcolap(a, k, n):
    cnt, arr = bin(k)
    b = 1
    if k == 0:
        return 0
    A = a
    if arr[0] == 1:
        b = a 
    for i in range(cnt):
        A = (A * A) % n
        if arr[i] == 1:
            b = (A * b) % n
    return b

def miller(n, t):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s, r = phantich(n)
    for i in range(t):
        a = random.randint(2, n - 2)
        y = nhanbinhphuongcolap(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = nhanbinhphuongcolap(y, 2, n)
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True

def distance(A):
    min_distance = 10000000  # Đổi tên biến từ min thành min_distance
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
