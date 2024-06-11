import math
def checknto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def binhphuongcolap(a, k, n):
    if a % n == 0:
        return 0
    b = 1
    A = a
    while(k != 0):
        if k % 2 == 1:
            b = (A * b) % n
        A = (a * A) % n
        k = k // 2
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
