import math

def eratosthenes(n):
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    return [i for i in range(2, n + 1) if primes[i]]

def check(N):
    primes = eratosthenes(N)
    for i in primes:
        if N % i == 0:
            if N % (i * i) != 0:
                return False
    return True

if __name__ == '__main__':
    N = 20  # cho trước < 10000
    cnt = 1
    for i in range(2, N):
        result = check(i)
        if result:
            print(f'Đây là số mạnh mẽ thứ {cnt} nhỏ hơn {N}:', i)
            cnt += 1
    if cnt == 1:
        print(f'Không có số nào mạnh hơn {N}')
