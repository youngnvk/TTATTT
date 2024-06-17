import random
def bin(n):
    arr = []
    cnt = 0
    while(n != 0):
        r = n % 2
        arr.append(r)
        cnt += 1
        n = n // 2
    return cnt, arr
def binhphuongcolap(a, k, n):
    cnt, arr = bin(k)
    b = 1
    if k == 0:
        return b
    A = a
    if arr[0] == 1:
        b = a
    for i in range(1, cnt):
        A = (A * A) % n
        if arr[i] == 1:
            b = (A * b) % n
    return b
def fermat(n, t):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for i in range(t):
        a = random.randint(2, n - 2)
        if binhphuongcolap(a, n - 1, n) != 1:
            return False
    return True
n = int(input('Nhap n: '))
t = int(input('So lan lap: '))
k = fermat(n, t)
if k:
    print('Nguyen to')
else:
    print('Hop so')