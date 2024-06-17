import math
import random
def bin(n):  # Chuyển đổi số nguyên sang dạng nhị phân
    arr2 = []
    cnt = 0
    while n != 0:
        r = n % 2
        arr2.append(r)
        cnt += 1
        n = n // 2
    return cnt, arr2

def modulo(a, k, n):  # Hàm tính lũy thừa modulo bằng phương pháp bình phương và nhân
    cnt, arr2 = bin(k)
    b = 1
    if k == 0:
        return 1  # 0^0 là 1 theo định nghĩa
    A = a
    if arr2[0] == 1:
        b = a 
    for i in range(1, cnt):  # Bắt đầu từ phần tử thứ hai
        A = (A * A) % n
        if arr2[i] == 1:
            b = (A * b) % n
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
    min_distance = 1000000000  
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            k = abs(A[i] - A[j])
            if min_distance > k:
                min_distance = k
    return min_distance
def list_primes(start, end, t, n):
    primes = []
    cnt = 0
    while(True):
        if cnt == n:
            break
        i = random.randint(start, end)
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
