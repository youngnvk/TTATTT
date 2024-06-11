import math

def checknto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def bin(n):
    arr = []
    cnt = 0
    while(n != 0):
        r = n % 2
        arr.append(r)
        cnt += 1
        n = n / 2
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
if __name__ == '__main__':
    a = int(input('Nhap a: '))
    k = int(input('Nhap k: '))
    n = int(input('Nhap n: '))
    test = binhphuongcolap(a, k, n)
    if test:
        print('Nguyen to')
    else:
        print('Hop so')
