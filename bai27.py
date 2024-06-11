import math
def gcd2(a, b):
    A = a
    B = b
    while(B > 0):
        R = A % B
        A = B
        B = R
    return A
def checkNto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
if __name__== '__main__':
    cnt = 0
    for i in range(1, 1000):
        for j in range(i + 1, 1000):
            gcd_a_b = gcd2(i, j)
            if checkNto(gcd_a_b):
                cnt += 1
                print(f'cặp số thứ {cnt} là: {(i, j)}')
                print('')