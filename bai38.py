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
    if gcd(a, b) != 1:
        return False
    u = a
    v = p
    x1 = 1
    x2 = 0
    if u == 0:
        return False
    while u != 1:
        q = v // u
        r = v - q * u
        x = x2 - q * x1
        v = u
        u = r
        x2 = x1
        x1 = x
    return x1 % p
if __name__=='__main__':
    while(True):
        a = int(input('Nhap a sao cho a > 0: '))
        if a > 0:
            p = int(input('Nhap p : '))
            break
        else:
            print('Nhap lai a!')
    b = nghichdao(a, p)
    if gcd(a, p) == 1:
        print(f'nghich dao cua {a} la {b}')