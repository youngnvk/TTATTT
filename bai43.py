import math
import random
def bin(n):
    cnt = 0
    arr = []
    while(n != 0):
        r = n % 2
        arr.append(r)
        n = n // 2
        cnt += 1
    return cnt, arr
def modulo(a, k, n):
    cnt, arr = bin(n)
    b = 1
    if k == 0:
        return 0
    A = a
    if arr[0] == 1:
        b = a 
    for i in range(cnt):
        A = (a * A) % n
        if arr[i] == 1:
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
    if n == 1 or n % 2 == 0:
        return False
    s, r = phantich(n) #chuan bi s va r
    for i in range(t):
        a = random.randint(2, n - 2)
        y = modulo(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = modulo(y, 2, 1)
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True
def random_prime(n, t):
    while True:
        a = random.randint(2, n - 2)
        if miller(a, t):
            return a
if __name__=='__main__':
    t = int(input('Nhap so lan lap: '))
    while(True):
        n = int(input('Nhap N: '))
        if 0 < n < 1000:
            break
        else:
            print('Moi ban nhap lai!')
    p = random_prime(n, t)
    ok = False
    for a in range(n):
        k = modulo(a, p, n)
        if miller(k, t):
            print(f"a = {a}, thỏa mãn {a} ^ {p} % {n} = {k} là số nguyên tố")
            print('')
            ok = True
    if not ok:
        print('Khong co so nao thoa man! ~')  
        