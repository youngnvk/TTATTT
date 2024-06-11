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
    A = int(input('Nhập A: '))
    B = int(input('Nhập B: ')) 
    cnt = 0
    for i in range(A, B + 1):
        primes = eratosthenes(i)
        count_fake = count(primes)
        if checknto(count_fake):
            cnt += 1
            print(f'số {i} là số siêu nguyên tố vì có số lượng số nto là {count_fake}')            
    print(cnt)
