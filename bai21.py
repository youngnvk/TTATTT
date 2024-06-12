import math
def eratosthenes(n):
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    return primes
def count(primes):
    cnt = 0
    for i in primes:
        if i == 1:
            cnt += 1
    return cnt
def checknto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    while(True):
        A = int(input('Nhập A: '))
        if A > 0:
            break
        else:
            print('Nhập lại !')
    while(True):
        B = int(input('Nhập A: '))
        if B > A:
            break
        else:
            print('Nhập lại !')
    cnt = 0
    for i in range(A, B + 1):
        primes = eratosthenes(i)
        dem = count(primes)
        if checknto(dem):
            print(f'số {i} là số siêu nguyên tố vì có số lượng số nguyên tố < {i} là {dem}')            
