import math
def gcd2(a, b):
    A = a
    B = b
    while B > 0:
        R = A % B
        A = B
        B = R
    return A
if __name__ == '__main__':
    M = int(input('Nhập M (0 < M < 1000): '))
    N = int(input('Nhập N (0 < N < 1000): '))
    D = int(input('Nhập D (0 < D < 1000): '))
    cnt = 0
    for i in range(M, N + 1):
        for j in range(i, N + 1):
            if gcd2(i, j) == D:
                cnt+= 1
                print(f'({i}, {j})')
                print ('')
                print(cnt)
    
    