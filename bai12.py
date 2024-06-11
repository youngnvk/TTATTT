
import math
def eratosthenes(n):
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    return [i for i in range(2, n + 1) if primes[i]]
def checkNto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True
if __name__=='__main__':
    n = int(input('Nhập giá trị của N: '))
    primes = eratosthenes(n)
    found = False
    for i in range(len(primes) - 3):
        sum = primes[i] + primes[i + 1] + primes[i + 2] + primes[i + 3]
        if checkNto(sum) and sum <= n:
            print(primes[i], primes[i + 1], primes[i + 2], primes[i + 3])
            found = True
    if not found:
        print("Đéo tìm thấy!")
    